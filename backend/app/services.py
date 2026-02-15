import requests

def legal_ai_engine(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    if response.status_code != 200:
        return "Error contacting local LLM"

    data = response.json()
    return data.get("response", "No response")
