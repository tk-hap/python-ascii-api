from pydantic import BaseModel


class ASCII_Art(BaseModel):
    name: str
    ascii: str