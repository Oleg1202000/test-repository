from enum import Enum

from fastapi import FastAPI

items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World!'}


@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = [item_id]
    if q:
        item.append(q)
    if not short:
        item.append({"description": "This is an amazing item that has a long description"})
    return item


@app.get('/users/me')
async def read_user_me():
    return {"user_id": "the current user"}


@app.get('/users/{user_id}')
async def read_user_me(user_id: str):
    return {"user_id": user_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
