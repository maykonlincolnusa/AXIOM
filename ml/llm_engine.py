from ml.mini_model import MiniModel
from ml.user_classifier import UserClassifier

class LLMEngine:
    def __init__(self):
        self.model = MiniModel()
        self.classifier = UserClassifier()

    def chat(self, message: str) -> dict:
        category = self.classifier.classify(message)
        response = self.model.generate(message)
        return {
            "category": category,
            "response": response
        }

