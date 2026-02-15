import streamlit as st

st.title("Teste do Streamlit")
user_input = st.text_input("Escreva algo:")
if user_input:
    st.write("Você escreveu:", user_input)
