class MiniModel:
    def __init__(self):
        self.memory = []

    def generate(self, text: str) -> str:
        self.memory.append(text)
        return f"Resposta simulada para: {text}"
