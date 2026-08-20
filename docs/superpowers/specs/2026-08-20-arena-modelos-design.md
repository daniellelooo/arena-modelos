# Arena de modelos gratuitos de OpenRouter — diseño

Fecha: 2026-08-20
Tipo: experimento descartable (carpeta `IA/`)

## Qué es

Script de terminal en Python. REPL interactivo: el usuario escribe un prompt, se manda
en paralelo a varios modelos `:free` de OpenRouter, se imprimen las respuestas lado a
lado (modelo, latencia, tokens), y un modelo juez elige la mejor respuesta sin saber qué
modelo la escribió, con una justificación breve.

## Estructura

```
arena.py          # REPL: loop de input, orquesta la llamada y el print
config.py         # lista de modelos :free + modelo juez, timeouts
client.py         # llamada a OpenRouter (requests), maneja error/timeout por modelo
requirements.txt  # requests, python-dotenv
.env.example       # OPENROUTER_API_KEY=
.gitignore         # .env, __pycache__/, venv/
README.md         # qué es, instalación, cómo correrlo
```

## Modelos

Lista fija en `config.py`, familias distintas, todos con sufijo `:free`:

- `meta-llama/llama-3.3-70b-instruct:free`
- `google/gemini-2.0-flash-exp:free`
- `deepseek/deepseek-r1:free`
- `qwen/qwen-2.5-72b-instruct:free`
- Juez: `mistralai/mistral-small-3.1-24b-instruct:free`

## Flujo

1. Usuario escribe un prompt en el REPL (o `salir` para terminar).
2. `ThreadPoolExecutor` dispara las 4 llamadas en paralelo (`client.call_model`).
3. Cada resultado trae texto, latencia y tokens (si la API los devuelve).
4. Se imprimen las 4 respuestas.
5. Se arma un prompt con las respuestas etiquetadas A/B/C/D (sin nombre de modelo) y se
   manda al modelo juez.
6. Se imprime el veredicto del juez y cuál modelo era en realidad cada letra.

## Manejo de errores

Si un modelo falla o da timeout (los `:free` tienen rate limits agresivos), esa
respuesta se marca como "no disponible" y la arena sigue con los demás. No se cae toda
la ejecución por un modelo caído.

## Fuera de alcance

Sin tests formales, sin UI web, sin persistencia de resultados. Es un experimento para
probar modelos gratuitos, no una herramienta productizada.
