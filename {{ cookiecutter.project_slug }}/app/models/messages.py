from typing import List
from pydantic import BaseModel
from langchain_core.messages import BaseMessage
from .message import Message


class Messages(BaseModel):
    """A collection of messages."""

    content: List[Message]

    def to_langchain(self):
        """Convert the messages to a LangChain messages."""
        return [message.to_langchain() for message in self.content]
    
    @staticmethod
    def from_langchain(messages: List[BaseMessage]):
        """Convert a LangChain messages to a Messages."""
        return Messages(content=[Message.from_langchain(message) for message in messages])
