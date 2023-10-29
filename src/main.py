from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from models import ASCII_Art

ascii_api = FastAPI()

art_dict = []


@ascii_api.get("/")
async def root():
    return {"message": "Hello World"}


@ascii_api.get("/art")
async def get_art():
    return art_dict

@ascii_api.post("/art")
async def add_art():
    return {"message": "Art added successfully"}

@ascii_api.get("/art/{art_id}", response_class=PlainTextResponse)
async def read_art(art_id: str) -> str:
    return art_dict[art_id]
