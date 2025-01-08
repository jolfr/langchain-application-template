import os
from langchain_openai import ChatOpenAI

model = None

def init_model():
    """
    Initializes the model for the chain.
    """
    global model
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.environ.get("OPENAI_API_KEY"),
    )