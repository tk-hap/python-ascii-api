from pydantic import BaseModel


class ASCII_Art(BaseModel):
    name: str
    ascii_b64: str
    artist: str