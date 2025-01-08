from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

system_prompt = [
    SystemMessage(content="You are a helpful assistant."),
]

def get_prompt(message: HumanMessage):
    """
    Get the prompt for the chain.

    Args:
        message (HumanMessage): The message to add to the prompt.

    Returns:
        list[BaseMessage]: The prompt for the chain.
    """
    return system_prompt + [message]