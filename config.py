"""Configuración de la arena: qué modelos gratuitos de OpenRouter se enfrentan."""

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Familias distintas para que la comparación tenga sentido.
# OpenRouter rota este catálogo seguido — si un modelo empieza a dar 404
# ("unavailable for free" o "no endpoints found"), revisa la lista viva:
#   curl -s https://openrouter.ai/api/v1/models | python3 -c \
#     "import json,sys; [print(m['id']) for m in json.load(sys.stdin)['data'] if m['id'].endswith(':free')]"
MODELS = [
    {"id": "openai/gpt-oss-20b:free", "name": "GPT-OSS 20B"},
    {"id": "google/gemma-4-31b-it:free", "name": "Gemma 4 31B"},
    {"id": "z-ai/glm-5.2:free", "name": "GLM 5.2"},
    {"id": "nvidia/nemotron-3-super-120b-a12b:free", "name": "Nemotron 3 Super 120B"},
]

JUDGE_MODEL = {"id": "nvidia/nemotron-3-nano-30b-a3b:free", "name": "Nemotron 3 Nano 30B"}

TIMEOUT_SECONDS = 60
