from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Agentic RAG Assistant"
    app_version: str = "0.1.0"
    debug: bool = True

    llm_provider: str = "ollama"
    llm_model: str = "llama3.1"

    embedding_provider: str = "sentence-transformers"
    embedding_model: str = "BAAI/bge-base-en-v1.5"

    vector_db: str = "qdrant"
    qdrant_url: str = "http://localhost:6333"

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()