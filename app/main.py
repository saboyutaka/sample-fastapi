from typing import List, Optional
from enum import Enum
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
                "tags": ["coffee", "been"]
            }
        }


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{num}")
async def hello(num: int):
    return {"message": "Hello World"}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/items/")
async def create_item(item: Item = Body(..., embed=True)):
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user
