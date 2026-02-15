import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

texts = [
    "Inteligência artificial é a área que cria sistemas inteligentes",
    "Machine learning aprende padrões a partir de dados",
    "Redes neurais são inspiradas no cérebro humano",
    "IA pode ser usada em medicina, segurança e negócios",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

joblib.dump(vectorizer, "ml/model.pkl")

print("Modelo salvo em ml/model.pkl")
