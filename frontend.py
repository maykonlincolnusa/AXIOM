import streamlit as st
import requests
from datetime import datetime

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Axiom AI",
    page_icon="⚖️",
    layout="wide",
)

# ---------- STYLE ----------
st.markdown("""
<style>
    html, body, [class*="css"]  {
        background-color: #0e1117;
        color: white;
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #8a2be2, #c77dff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        font-size: 1.1rem;
        opacity: 0.85;
    }

    .chat-box {
        background: rgba(255,255,255,0.03);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 12px;
        border: 1px solid rgba(255,255,255,0.06);
    }

    .user {
        color: #c77dff;
        font-weight: 600;
    }

    .bot {
        color: #00ffd5;
        font-weight: 600;
    }

    .timestamp {
        font-size: 0.7rem;
        opacity: 0.4;
    }

    textarea {
        border-radius: 12px !important;
        background: #111 !important;
        color: white !important;
    }

    .stButton>button {
        background: linear-gradient(135deg, #8a2be2, #5a189a);
        border-radius: 12px;
        font-weight: 600;
        height: 48px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## ⚖️ **Axiom AI**")
    st.markdown("### Intelligent Legal Assistant")
    st.divider()
    st.markdown("**Capabilities:**")
    st.markdown("- Legal research")
    st.markdown("- Document analysis")
    st.markdown("- Case reasoning")
    st.markdown("- Compliance support")
    st.divider()
    st.markdown("**Tech Stack:**")
    st.markdown("- FastAPI")
    st.markdown("- LLM Agents")
    st.markdown("- Vector Search")
    st.markdown("- Streamlit UI")
    st.divider()
    st.markdown("🧠 *Built by Maykon Lincoln*")

# ---------- HEADER ----------
st.markdown('<div class="title">Axiom AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Next-generation legal intelligence powered by AI</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- CHAT HISTORY ----------
for msg in st.session_state.messages:
    st.markdown(f"""
    <div class="chat-box">
        <span class="{msg['role']}">{msg['role'].upper()}</span><br>
        {msg['content']}<br>
        <span class="timestamp">{msg['time']}</span>
    </div>
    """, unsafe_allow_html=True)

# ---------- INPUT ----------
question = st.text_area(
    "Ask a legal question",
    height=100,
    placeholder="Ex: Can an employee be terminated without cause under Brazilian labor law?"
)

# ---------- SEND ----------
if st.button("Send"):
    if question.strip():
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.messages.append({
            "role": "user",
            "content": question,
            "time": timestamp
        })

        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/legal",
                    json={"question": question},
                    timeout=180
                )
                data = response.json()

                answer = data.get("answer", "No response generated.")

                st.session_state.messages.append({
                    "role": "bot",
                    "content": answer,
                    "time": datetime.now().strftime("%H:%M:%S")
                })

                st.experimental_rerun()

            except Exception as e:
                st.error(f"Backend error: {e}")
