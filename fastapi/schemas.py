from datetime import date
from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None #Field(default=None, max_length=200)
    price: float
    tax: float | None = None
    date: date
    tag: set[str] = set()
    image: Image | None = None

'''
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
'''

class User(BaseModel):
    username: str
    full_name: str | None = None