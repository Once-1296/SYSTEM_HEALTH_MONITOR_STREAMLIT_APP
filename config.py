import os
from dotenv import load_dotenv

load_dotenv()

class OllamaConfig:
    BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    MODEL_NAME = os.getenv("MODEL_NAME", "mistral")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
