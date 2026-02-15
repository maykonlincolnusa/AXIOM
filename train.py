import joblib
from model import create_model

X = [
    "oi",
    "olá",
    "bom dia",
    "tudo bem?",
    "qual seu nome",
    "o que você faz",
    "me fale sobre IA",
    "o que é machine learning",
]

y = [
    "saudacao",
    "saudacao",
    "saudacao",
    "saudacao",
    "identidade",
    "identidade",
    "ia",
    "ia",
]

model = create_model()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Modelo treinado e salvo")
