from fastapi import APIRouter
from .schemas import LegalRequest, LegalResponse
from .services import legal_ai_engine

router = APIRouter(prefix="/api")

@router.post("/legal", response_model=LegalResponse)
def legal_assistant(data: LegalRequest):
    answer = legal_ai_engine(data.question)
    return {"answer": answer}
