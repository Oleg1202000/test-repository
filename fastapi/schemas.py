from datetime import date
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, max_length=20)
    price: float
    tax: float | None = None
    date: date


class User(BaseModel):
    username: str
    full_name: str | None = None