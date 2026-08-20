"""Configuración de la arena: qué modelos gratuitos de OpenRouter se enfrentan."""

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Familias distintas para que la comparación tenga sentido.
# Si alguno deja de estar disponible como :free, cámbialo aquí.
MODELS = [
    {"id": "meta-llama/llama-3.3-70b-instruct:free", "name": "Llama 3.3 70B"},
    {"id": "google/gemini-2.0-flash-exp:free", "name": "Gemini 2.0 Flash"},
    {"id": "deepseek/deepseek-r1:free", "name": "DeepSeek R1"},
    {"id": "qwen/qwen-2.5-72b-instruct:free", "name": "Qwen 2.5 72B"},
]

JUDGE_MODEL = {"id": "mistralai/mistral-small-3.1-24b-instruct:free", "name": "Mistral Small 3.1"}

TIMEOUT_SECONDS = 60
