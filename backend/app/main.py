from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Axiom AI Backend")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok", "message": "Axiom backend running"}
