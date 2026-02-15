from app.agents.legal import legal_agent
from app.agents.finance import finance_agent
from app.agents.real_estate import real_estate_agent

def route_question(question: str):
    q = question.lower()

    if any(word in q for word in ["processo", "lei", "direito", "advogado", "contrato"]):
        return legal_agent(question)

    if any(word in q for word in ["investimento", "dinheiro", "renda", "juros", "finança"]):
        return finance_agent(question)

    if any(word in q for word in ["imóvel", "apartamento", "casa", "aluguel", "financiamento"]):
        return real_estate_agent(question)

    return legal_agent(question)  # fallback inteligente
