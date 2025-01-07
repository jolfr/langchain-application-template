from fastapi import APIRouter

from app.models import RequestMessage

router = APIRouter()

@router.post("/")
async def chat(message: RequestMessage):
    """Chat endpoint to send a message to the LLM."""
    message = message.to_message()
    return {"message": message}
