from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    API_NAME: str = "Axiom"
    API_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Security
    SECRET_KEY: str = "CHANGE_ME"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # OpenAI / LLM
    LLM_PROVIDER: str = "openai"
    OPENAI_API_KEY: str | None = None

    # Database (se quiser depois)
    DATABASE_URL: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
