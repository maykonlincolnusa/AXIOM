from pydantic import BaseModel

class LegalRequest(BaseModel):
    question: str

class LegalResponse(BaseModel):
    answer: str
