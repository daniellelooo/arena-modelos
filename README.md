# Arena de modelos gratuitos de OpenRouter

Experimento de terminal: mandas el mismo prompt a varios modelos `:free` de OpenRouter
en paralelo, ves las respuestas lado a lado (latencia, tokens), y un modelo juez elige
la mejor sin saber qué modelo la escribió.

## Modelos incluidos

Ver [`config.py`](config.py). Por defecto: GPT-OSS 20B, Gemma 4 31B, GLM 5.2 y Nemotron 3
Super 120B, con Nemotron 3 Nano 30B como juez.

OpenRouter rota el catálogo `:free` seguido — si un modelo empieza a dar 404, revisa la
lista viva y cambia el slug en `config.py`:

```bash
curl -s https://openrouter.ai/api/v1/models | python3 -c \
  "import json,sys; [print(m['id']) for m in json.load(sys.stdin)['data'] if m['id'].endswith(':free')]"
```

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
