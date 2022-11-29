from enum import Enum
from typing import List

from fastapi import FastAPI, Query

from schemas import Item


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


@app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: bool = False):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result['price'] = item.price * 0.9
    return result


@app.get('/items/')
async def read_items(q: str = Query(alias='item-query')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
