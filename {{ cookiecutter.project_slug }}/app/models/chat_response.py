from pydantic import BaseModel, field_validator

from langchain_core.messages import AIMessage

class ChatResponse(BaseModel):
    message: str
    tokens: int

    @field_validator("message")
    def validate_message(cls, v):
        if not v:
            raise ValueError("Message cannot be empty")
        return v

    @field_validator("tokens")
    def validate_tokens(cls, v):
        if v <= 0:
            raise ValueError("Tokens must be greater than 0")
        return v
    
    @staticmethod
    def from_chain_response(response: AIMessage):
        try:
            return ChatResponse(message=response.content, tokens=response.usage_metadata["total_tokens"])
        except Exception:
            raise ValueError("Invalid response from chain")