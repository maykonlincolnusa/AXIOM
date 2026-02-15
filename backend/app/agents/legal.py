from app.llm.ollama import ask_ollama

def legal_agent(question: str):
    prompt = f"""
Você é um assistente jurídico especializado em direito brasileiro.
Responda com clareza, objetividade e precisão.

Pergunta:
{question}
"""
    return ask_ollama(prompt)
