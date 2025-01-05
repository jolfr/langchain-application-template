import pytest
from app.models.message import Message, Roles
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage

def test_create_message():
    """Test creating a message."""
    message = Message(content="Hello, world!", role="user")
    assert message.content == "Hello, world!"
    assert message.role == Roles.USER

def test_create_message_with_invalid_role():
    """Test creating a message with an invalid role."""
    with pytest.raises(ValueError) as e:
        Message(content="Hello, error!", role="invalid")
    assert "Input should be" in str(e.value)

def test_create_message_with_missing_content():
    """Test creating a message with missing content."""
    with pytest.raises(ValueError) as e:
        Message(role="user")
    assert "Field required" in str(e.value)

def test_create_message_with_missing_role():
    """Test creating a message with missing role."""
    with pytest.raises(ValueError) as e:
        Message(content="Hello, world!")
    assert "Field required" in str(e.value)

def test_user_message_to_langchain():
    """Test converting a user message to a LangChain message and back."""
    message = Message(content="Hello, world!", role="user")
    langchain_message = message.to_langchain()
    assert isinstance(langchain_message, HumanMessage)
    assert langchain_message.content == "Hello, world!"

    message_from_langchain = Message.from_langchain(langchain_message)
    assert message_from_langchain.content == message.content
    assert message_from_langchain.role == message.role

def test_ai_message_to_langchain():
    """Test converting an AI message to a LangChain message and back."""
    message = Message(content="Hello, world!", role="assistant")
    langchain_message = message.to_langchain()
    assert isinstance(langchain_message, AIMessage)
    assert langchain_message.content == "Hello, world!"

    message_from_langchain = Message.from_langchain(langchain_message)
    assert message_from_langchain.content == message.content
    assert message_from_langchain.role == message.role

def test_system_message_to_from_langchain():
    """Test converting a system message to a LangChain message and back."""
    message = Message(content="Hello, world!", role="system")
    langchain_message = message.to_langchain()
    assert isinstance(langchain_message, SystemMessage)
    assert langchain_message.content == "Hello, world!"

    message_from_langchain = Message.from_langchain(langchain_message)
    assert message_from_langchain.content == message.content
    assert message_from_langchain.role == message.role

def test_tool_message_to_langchain():
    """Test converting a tool message to a LangChain message and back."""
    message = Message(content="Hello, world!", role="tool", tool_call_id="123")
    langchain_message = message.to_langchain()
    assert isinstance(langchain_message, ToolMessage)
    assert langchain_message.content == "Hello, world!"
    assert langchain_message.tool_call_id == "123"

    message_from_langchain = Message.from_langchain(langchain_message)
    assert message_from_langchain.content == message.content
    assert message_from_langchain.role == message.role
    assert message_from_langchain.tool_call_id == message.tool_call_id
