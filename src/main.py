from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
import stream_chat

from .settings import settings
from .models import TokenResponse

server_client = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global server_client

    server_client = stream_chat.StreamChat(
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET,
    )
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return "Welcome to the Stream Token Generator"


@app.get("/token/{user_id}")
def get_token(user_id: str):

    print(server_client)

    if server_client is None:
        raise HTTPException(status_code=500, detail="Server not started successfully")

    token = server_client.create_token(user_id)

    return TokenResponse(token=token)
