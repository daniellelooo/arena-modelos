"""Arena de modelos gratuitos de OpenRouter. REPL: escribe un prompt, compara respuestas."""

import os
import string
import sys
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv

from client import call_model
from config import JUDGE_MODEL, MODELS

load_dotenv()

LETTERS = string.ascii_uppercase


def run_round(prompt: str) -> None:
    with ThreadPoolExecutor(max_workers=len(MODELS)) as pool:
        results = list(pool.map(lambda m: call_model(m["id"], prompt), MODELS))

    print()
    for model, result in zip(MODELS, results):
        retries = result.get("retries", 0)
        suffix = f", {retries} reintento(s)" if retries else ""
        print(f"--- {model['name']} ({result['latency_ms']} ms{suffix}) ---")
        if result["ok"]:
            tokens = result["tokens"]
            if tokens is not None:
                print(f"[{tokens} tokens]")
            print(result["text"].strip())
        else:
            print(f"[no disponible: {result['error']}]")
        print()

    judge(prompt, results)


def judge(prompt: str, results: list[dict]) -> None:
    ok_results = [(letter, model, r) for letter, model, r in
                  zip(LETTERS, MODELS, results) if r["ok"]]

    if len(ok_results) < 2:
        print("(no hay suficientes respuestas válidas para que el juez compare)")
        return

    labeled = "\n\n".join(
        f"Respuesta {letter}:\n{r['text'].strip()}" for letter, _, r in ok_results
    )
    judge_prompt = (
        f"Pregunta original: {prompt}\n\n"
        f"Estas son varias respuestas de distintos modelos de IA a esa pregunta:\n\n"
        f"{labeled}\n\n"
        "¿Cuál respuesta es mejor? Responde solo con la letra y una justificación de "
        "una o dos frases."
    )

    print(f"=== Veredicto del juez ({JUDGE_MODEL['name']}) ===")
    verdict = call_model(JUDGE_MODEL["id"], judge_prompt)
    if not verdict["ok"]:
        print(f"[juez no disponible: {verdict['error']}]")
        return

    print(verdict["text"].strip())
    print()
    print("Referencia (letra -> modelo real):")
    for letter, model, _ in ok_results:
        print(f"  {letter} = {model['name']}")
    print()


def main() -> None:
    print("Arena de modelos gratuitos de OpenRouter. Escribe 'salir' para terminar.\n")
    while True:
        try:
            prompt = input("prompt> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not prompt:
            continue
        if prompt.lower() in {"salir", "exit", "quit"}:
            break

        run_round(prompt)


if __name__ == "__main__":
    if "OPENROUTER_API_KEY" not in os.environ:
        print("Falta OPENROUTER_API_KEY. Copia .env.example a .env y pon tu key.")
        sys.exit(1)
    main()
