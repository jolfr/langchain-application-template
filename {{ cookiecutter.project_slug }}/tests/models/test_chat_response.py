import pytest
from langchain_core.messages import AIMessage
from app.models import ChatResponse

def test_create_chat_response():
    response = ChatResponse(message="Hello, world!", tokens=100)
    assert response.message == "Hello, world!"
    assert response.tokens == 100

def test_create_chat_response_with_no_message():
    with pytest.raises(ValueError):
        ChatResponse(tokens=100)

def test_create_chat_response_with_empty_message():
    with pytest.raises(ValueError):
        ChatResponse(message="", tokens=100)

def test_create_chat_response_with_no_tokens():
    with pytest.raises(ValueError):
        ChatResponse(message="Hello, world!")

def test_create_chat_response_with_negative_tokens():
    with pytest.raises(ValueError):
        ChatResponse(message="Hello, world!", tokens=-1)

def test_create_chat_response_from_chain_response():
    chain_response = AIMessage(
        content="Hello! How can I assist you today?",
        usage_metadata={
            "input_tokens": 20,
            "output_tokens": 10,
            "total_tokens": 30,
            "input_token_details": {
                "audio": 0,
                "cache_read": 0
            },
            "output_token_details": {
                "audio": 0,
                "reasoning": 0
            }
        }
    )
    response = ChatResponse.from_chain_response(chain_response)
    assert response.message == "Hello! How can I assist you today?"
    assert response.tokens == 30