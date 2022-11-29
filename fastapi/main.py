from enum import Enum
from typing import List

from fastapi import FastAPI, Query, Path, Body

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


@app.get('/items/{item_id}')
async def read_items(
        item_id: int = Path(title='The ID of the item to get', gt=0, le=1000),
        q: str = Query(alias='item-query', deprecated=True)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
