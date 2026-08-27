from fastapi import FastAPI

from app.config.settings import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


@app.get("/")
def root():
    return {
        "message": "Agentic RAG Assistant is running!",
        "version": settings.app_version
    }