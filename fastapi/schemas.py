from datetime import date
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    date: date


class User(BaseModel):
    username: str
    full_name: str | None = None