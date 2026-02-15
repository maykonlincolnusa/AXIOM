from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

# 1. Dados de treinamento (Exemplos manuais para ensinar o modelo)
# No futuro, isso virá do seu banco de dados 'database.py'
X_train = [
    "Minha encomenda está atrasada, preciso pra ontem!",
    "Onde está meu pacote? É urgente.",
    "Qual o preço do frete para SP?",
    "Gostaria de saber o prazo de entrega.",
    "Isso é um absurdo, quero cancelar agora!",
    "Bom dia, tudo bem? Como funciona o envio?"
]
y_train = ["urgente", "urgente", "normal", "normal", "urgente", "normal"]

# 2. Criar Pipeline (Transforma texto em números -> Aplica Regressão Logística)
# Regressão Logística é excelente para classificação binária simples
model = make_pipeline(CountVectorizer(), LogisticRegression())

# 3. Treinar
print("Treinando classificador de usuários...")
model.fit(X_train, y_train)

# 4. Salvar o modelo para usar no app.py
joblib.dump(model, "user_classifier.pkl")

# 5. Função para usar no seu chat
def classificar_usuario(mensagem):
    modelo_carregado = joblib.load("user_classifier.pkl")
    predicao = modelo_carregado.predict([mensagem])[0]
    return predicao

# Teste
print(f"Mensagem: 'O caminhão quebrou, socorro!' -> Classificação: {classificar_usuario('O caminhão quebrou, socorro!')}")