import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt: str, model: str = "tinyllama"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)

    return response.json()["response"]
