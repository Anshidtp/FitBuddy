from langchain_community.chat_models import ChatOllama

# Utility function to get Ollama LLM
def get_ollama_llm(model_name="tinyllama"):
    return ChatOllama(model=model_name)