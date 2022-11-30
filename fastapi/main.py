from enum import Enum
from typing import List

from fastapi import FastAPI, Query, Path, Body, Cookie, Header, Form, File, UploadFile

from schemas import Item, User


items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World!'}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

'''
@app.get('/items/{item_id}')
async def read_items(
        item_id: int = Path(title='The ID of the item to get', gt=0, le=1000),
        q: str = Query(default=None, alias='item-query', deprecated=True)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
'''

@app.put('/items/{item_id}', tags=["items"])
async def update_item(*, item: Item = Body(
            examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
), item_id: int):
    results = {"item_id": item_id, "item": item}
    return results


@app.post('/items/', response_model=Item, response_model_exclude_unset=True, response_model_exclude_defaults=True)
async def create_item(item: Item):
    return item


@app.post('/login/')
async def login(username: str = Form(), password: str = Form()):
    return {'username': username}
