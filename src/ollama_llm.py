from langchain_ollama import OllamaLLM
# Make sure this is pulled and running via `ollama run tinyllama
# Default port

from dotenv import load_dotenv
import os

# Load environment
load_dotenv()
LLM_MODEL = os.getenv("LLM_MODEL")


def load_llm():
    return  OllamaLLM(model=LLM_MODEL, base_url="http://localhost:11434", temperature=0.7, max_tokens=512)
     

