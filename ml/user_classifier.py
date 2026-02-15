from sklearn.linear_model import LogisticRegression

def train_classifier(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model
