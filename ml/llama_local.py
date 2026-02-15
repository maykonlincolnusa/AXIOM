import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def llama_generate(prompt: str, model: str = "llama3.1:8b") -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    return response.json()["response"]
