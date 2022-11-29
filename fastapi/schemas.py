from datetime import date
from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, max_length=20)
    price: float
    tax: float | None = None
    date: date
    tag: set[str] = set()
    image: Image | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None