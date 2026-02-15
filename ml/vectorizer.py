from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def fit_texts(texts):
    return vectorizer.fit_transform(texts)

def transform(text):
    return vectorizer.transform([text])
