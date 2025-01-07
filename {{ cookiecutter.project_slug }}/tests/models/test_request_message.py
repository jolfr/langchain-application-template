from app.models import RequestMessage, Message
from app.models.message import Roles

def test_create_message():
    """Test creating a request message."""
    request = RequestMessage(content="Hello, world!")
    assert request.content == "Hello, world!"

def test_request_message_to_message():
    """Test converting a request message to a generic message."""
    request = RequestMessage(content="Hello, world!")
    message = request.to_message()
    assert isinstance(message, Message)
    assert message.content == "Hello, world!"
    assert message.role == Roles.USER
