from app.llm.ollama import OllamaLLM


llm = OllamaLLM()

response = llm.generate(
    "Explain what Retrieval-Augmented Generation is in one sentence."
)

print(response)