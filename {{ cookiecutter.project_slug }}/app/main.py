from fastapi import FastAPI
from .routers import chat_router

app = FastAPI()

# Include extra routers
app.include_router(chat_router, prefix="/chat")

@app.get("/")
async def healthcheck():
    """Healthcheck endpoint to verify API is running."""
    return {"status": "OK"}
