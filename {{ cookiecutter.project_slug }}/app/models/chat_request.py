from pydantic import BaseModel

from app.models.message import Message

class ChatRequest(BaseModel):
    """Request from chat endpoint."""
    message: str
    
    def to_message(self) -> Message:
        return Message(content=self.message, role="user")