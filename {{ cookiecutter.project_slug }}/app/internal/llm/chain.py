from langchain_core.messages import HumanMessage

from .prompt import get_prompt

def invoke_chain(message: HumanMessage):
    """
    Invoke the chain.

    Args:
        message (HumanMessage): The input message to respond to.

    Returns:
        str: The response from the chain.
    """
    from .model import model
    
    prompt = get_prompt(message)
    return model.invoke(prompt)