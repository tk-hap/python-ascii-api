from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import redis
import base64
from models import ASCII_Art

ascii_api = FastAPI()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@ascii_api.get("/healthcheck")
async def root() -> dict:
    return {"message": "healthy"}

@ascii_api.get("/art")
async def get_art() -> dict:
    all_items = [r.hgetall(x) for x in r.scan_iter("art:*")]
    return {"ascii_art": all_items}

@ascii_api.post("/art")
async def add_art(art: ASCII_Art) -> dict:
    r.hset(f"art:{art.name}", mapping={
        "name": art.name,
        "ascii_b64": art.ascii_b64,
        "artist": art.artist
    })
    return {"message": f"ASCII art {art.name} added"}

@ascii_api.get("/art/{art_id}", response_class=PlainTextResponse)
async def read_art(art_id: str) -> str:
    return base64.b64decode(r.hget(f"art:{art_id}", "ascii_b64"))
