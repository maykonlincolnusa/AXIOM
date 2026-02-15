import streamlit as st
import requests

st.set_page_config(page_title="Axiom AI", page_icon="⚖️", layout="centered")

st.title("⚖️ Axiom AI — Legal Assistant")
st.caption("LLM local com Ollama • Zero custo • 100% offline")

# Histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
prompt = st.chat_input("Digite sua pergunta jurídica...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "phi3:mini",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=120
                )
                answer = response.json()["response"]
            except Exception as e:
                answer = f"Erro: {e}"

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
