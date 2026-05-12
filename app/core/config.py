from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
     
    APP_NAME: str = Field(default="context-aware-rag")
    CHROMA_HOST: str = Field(default="localhost")
    CHROMA_PORT: int = Field(default=8001)
    EMBEDDING_MODEL: str = Field(default="all-MiniLM-L6-v2")
    TOP_K_RESULTS: int = Field(default=3)


settings = Settings()