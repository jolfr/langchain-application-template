from fastapi import APIRouter, HTTPException
import logging

from app.models import ChatRequest, ChatResponse
from app.internal import invoke_chain
router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/")
async def chat(request: ChatRequest):
    """Chat endpoint to send a message to the LLM."""
    langchain_message = request.to_message().to_langchain()
    try:
        response = invoke_chain(langchain_message)
    except Exception as e:
        logger.error(f"Error invoking chain: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return ChatResponse.from_chain_response(response)
