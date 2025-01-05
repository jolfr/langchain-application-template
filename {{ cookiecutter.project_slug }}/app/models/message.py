from typing import Optional
from pydantic import BaseModel
from enum import Enum
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ToolMessage
class Roles(Enum):
    """Enum for chat message roles."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"

class Message(BaseModel):
    """Chat message model."""
    content: str
    role: Roles
    tool_call_id: Optional[str] = None

    def to_langchain(self):
        """Convert the message to a LangChain message."""
        
        match self.role:
            case Roles.USER:
                return HumanMessage(content=self.content)
            case Roles.ASSISTANT:
                return AIMessage(content=self.content)
            case Roles.SYSTEM:
                return SystemMessage(content=self.content)
            case Roles.TOOL:
                return ToolMessage(content=self.content, tool_call_id=self.tool_call_id)
            case _:
                raise ValueError(f"Unknown role: {self.role}")

    @staticmethod
    def from_langchain(message: BaseMessage):
        """Convert a LangChain message to a Message."""

        if isinstance(message, HumanMessage):
            return Message(content=message.content, role=Roles.USER)
        elif isinstance(message, AIMessage):
            return Message(content=message.content, role=Roles.ASSISTANT)
        elif isinstance(message, SystemMessage):
            return Message(content=message.content, role=Roles.SYSTEM)
        elif isinstance(message, ToolMessage):
            return Message(content=message.content, role=Roles.TOOL, tool_call_id=message.tool_call_id)
        else:
            raise ValueError(f"Unknown message type: {type(message)}")