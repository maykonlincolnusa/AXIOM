from app.llm.ollama import ask_ollama

def finance_agent(question: str):
    prompt = f"""
Você é um consultor financeiro especializado em finanças pessoais,
investimentos, crédito e planejamento financeiro.

Pergunta:
{question}
"""
    return ask_ollama(prompt)
