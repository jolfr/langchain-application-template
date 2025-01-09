from app.models import ChatRequest, Message
from app.models.message import Roles

def test_create_chat_request():
    """Test creating a chat request."""
    request = ChatRequest(message="Hello, world!")
    assert request.message == "Hello, world!"

def test_chat_request_to_message():
    """Test converting a chat request to a message."""
    request = ChatRequest(message="Hello, world!")
    message = request.to_message()
    assert isinstance(message, Message)
    assert message.content == "Hello, world!"
    assert message.role == Roles.USER
