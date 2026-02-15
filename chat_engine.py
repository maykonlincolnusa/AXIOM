from ml.models.llama_local import llama_generate

def chat_engine(prompt: str) -> str:
    system_prompt = """
    You are a senior legal assistant specialized in global law.
    Answer clearly, objectively and professionally.
    """

    full_prompt = f"{system_prompt}\n\nUser: {prompt}\nAssistant:"

    return llama_generate(full_prompt)
