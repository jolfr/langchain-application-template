import os

if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set")

from langchain_openai import ChatOpenAI

def get_model():
    """
    Get the model for the chain.

    Returns:
        ChatOpenAI: The model for the chain.
    """
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.environ.get("OPENAI_API_KEY"),
    )