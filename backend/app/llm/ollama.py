import ollama

from app.config.settings import settings
from app.llm.base import BaseLLM


class OllamaLLM(BaseLLM):

    def __init__(self, model: str | None = None):
        self.model = model or settings.llm_model

    def generate(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]