from fastapi import FastAPI

ascii_api = FastAPI()

@ascii_api.get("/")
async def root():
    return {"message": "Hello World"}
