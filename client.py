"""Llamadas a OpenRouter. Cada llamada es independiente: si una falla, no tumba la arena."""

import os
import time

import requests

from config import OPENROUTER_URL, TIMEOUT_SECONDS


def call_model(model_id: str, prompt: str) -> dict:
    api_key = os.environ["OPENROUTER_API_KEY"]
    started = time.monotonic()

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model_id,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=TIMEOUT_SECONDS,
        )
        latency_ms = int((time.monotonic() - started) * 1000)

        if response.status_code != 200:
            return {
                "ok": False,
                "error": f"HTTP {response.status_code}: {response.text[:200]}",
                "latency_ms": latency_ms,
            }

        data = response.json()
        text = data["choices"][0]["message"]["content"]
        usage = data.get("usage", {})

        return {
            "ok": True,
            "text": text,
            "latency_ms": latency_ms,
            "tokens": usage.get("total_tokens"),
        }

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "timeout", "latency_ms": TIMEOUT_SECONDS * 1000}
    except requests.exceptions.RequestException as exc:
        latency_ms = int((time.monotonic() - started) * 1000)
        return {"ok": False, "error": str(exc), "latency_ms": latency_ms}
