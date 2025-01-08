from fastapi import APIRouter

from app.models import ChatRequest
from app.internal import invoke_chain
router = APIRouter()

@router.post("/")
async def chat(request: ChatRequest):
    """Chat endpoint to send a message to the LLM."""
    langchain_message = request.to_message().to_langchain()
    response = invoke_chain(langchain_message)
    return response
