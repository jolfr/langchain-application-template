from fastapi import FastAPI
from .routers import chat_router
from .internal import lifespan

app = FastAPI(lifespan=lifespan)

# Include extra routers
app.include_router(chat_router, prefix="/chat")

# Set up healthcheck endpoint
@app.get("/")
async def healthcheck():
    """Healthcheck endpoint to verify API is running."""
    return {"status": "OK"}
