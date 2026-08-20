# Arena de modelos gratuitos de OpenRouter

Experimento de terminal: mandas el mismo prompt a varios modelos `:free` de OpenRouter
en paralelo, ves las respuestas lado a lado (latencia, tokens), y un modelo juez elige
la mejor sin saber qué modelo la escribió.

## Modelos incluidos

Ver [`config.py`](config.py). Por defecto: Llama 3.3 70B, Gemini 2.0 Flash, DeepSeek R1
y Qwen 2.5 72B, con Mistral Small 3.1 como juez. Si alguno deja de estar disponible como
`:free`, cámbialo ahí.

## Instalación

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Pon tu API key de OpenRouter en `.env`:

```
OPENROUTER_API_KEY=sk-or-v1-...
```

## Uso

```bash
python arena.py
```

Escribe un prompt, revisa las respuestas y el veredicto del juez. Escribe `salir` para
terminar.

## Notas

Los modelos `:free` de OpenRouter tienen límites de uso agresivos (rate limits por
minuto y por día). Si un modelo falla o da timeout, la arena lo marca como "no
disponible" y sigue con los demás.
