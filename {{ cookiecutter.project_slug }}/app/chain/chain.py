from langchain_core.messages import BaseMessage, HumanMessage

from app.chain.model import get_model
from app.chain.prompt import get_prompt
model = get_model()

def invoke_chain(message: HumanMessage):
    """
    Invoke the chain.

    Args:
        message (HumanMessage): The input message to respond to.

    Returns:
        str: The response from the chain.
    """
    prompt = get_prompt(message)
    return model.invoke(prompt)
