from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def chat(message: str):
    """Chat endpoint to send a message to the LLM."""
    return {"message": message}
