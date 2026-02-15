def predict(text: str) -> str:
    text = text.lower()

    if any(w in text for w in ["oi", "olá", "ola", "bom dia", "boa tarde"]):
        return "Olá! 😊 Como posso te ajudar hoje?"

    if "quem é você" in text:
        return "Sou um Mini LLM criado para demonstrar um chat inteligente offline."

    if "como funciona" in text:
        return "Eu analiso sua pergunta e tento responder com base no conhecimento disponível."

    if "erro" in text or "problema" in text:
        return "Pode me explicar melhor o problema? Assim consigo te ajudar."

    return "Interessante 🤔 Pode me dar mais detalhes sobre isso?"
