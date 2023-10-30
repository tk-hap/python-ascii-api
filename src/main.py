from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import redis
from models import ASCII_Art

ascii_api = FastAPI()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@ascii_api.get("/")
async def root():
    return {"message": "Hello World"}


@ascii_api.get("/art")
async def get_art():
    return {"ascii_art": r.keys()}

@ascii_api.post("/art")
async def add_art(art: ASCII_Art):
    r.set(art.name, art.ascii)
    return {"message": "Art added successfully"}

@ascii_api.get("/art/{art_id}", response_class=PlainTextResponse)
async def read_art(art_id: str):
    return r.get(art_id)
