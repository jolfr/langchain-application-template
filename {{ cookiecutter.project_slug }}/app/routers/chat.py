from fastapi import APIRouter

from app.models import ChatRequest

router = APIRouter()

@router.post("/")
async def chat(request: ChatRequest):
    """Chat endpoint to send a message to the LLM."""
    message = request.to_message()
    return {"message": message}
