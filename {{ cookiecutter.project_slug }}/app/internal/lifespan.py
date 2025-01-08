from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from fastapi import FastAPI

from .llm.model import init_model

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load environment variables from .env file
    load_dotenv()
    
    # Check for OPEN_AI_API_KEY
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not set")
    
    # Initialize the model
    init_model()

    yield
    