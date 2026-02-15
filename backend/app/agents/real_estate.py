from app.llm.ollama import ask_ollama

def real_estate_agent(question: str):
    prompt = f"""
Você é um especialista em mercado imobiliário brasileiro.
Responda como um corretor profissional e consultor estratégico.

Pergunta:
{question}
"""
    return ask_ollama(prompt)
