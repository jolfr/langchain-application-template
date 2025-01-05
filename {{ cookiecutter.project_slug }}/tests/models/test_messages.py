from app.models import Messages, Message
from langchain_core.messages import HumanMessage
def test_create_messages():
    """Test creating a Messages."""
    messages = Messages(content=[Message(content="Hello, world!", role="user")])
    assert len(messages.content) == 1
    assert messages.content[0].content == "Hello, world!"

def test_messages_to_langchain():
    """Test converting a Messages to a LangChain list of messages."""
    messages = Messages(content=[Message(content="Hello, world!", role="user")])
    langchain_messages = messages.to_langchain()
    assert isinstance(langchain_messages, list)
    assert len(langchain_messages) == 1
    assert isinstance(langchain_messages[0], HumanMessage)
    assert langchain_messages[0].content == "Hello, world!"

def test_messages_from_langchain():
    """Test converting a LangChain list of messages to a Messages."""
    langchain_messages = [HumanMessage(content="Hello, world!")]
    messages = Messages.from_langchain(langchain_messages)
    assert isinstance(messages, Messages)
    assert len(messages.content) == 1
    assert messages.content[0].content == "Hello, world!"