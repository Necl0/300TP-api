from fastapi import FastAPI, Path
from pydantic import BaseModel
from inventoryb import *
import typing


class Poem(BaseModel):
    style: str
    author: str
    title: str
    content: str


# check on the actual inventory
print(poem_json)
# set up FastAPI and the actual API
app = FastAPI()

# home endpoint
@app.get("/")
def home() -> typing.Dict[str, str]:
    return {"Data":"Test"}

# about endpoint
@app.get("/about")
def about() -> typing.Dict[str, str]:
    return {"name": "MerolAPI", "info": "An API for Chinese philosophy quotes made using FastAPI.", "author": "Necloremius"}


# item based on ID endpoint
@app.get("/get-item/{poem_number}") # path parameter
def get_item(poem_number: int = Path(None, description="Number of poem that you would like to request data for.", gt=0, lt=321)):
    return poem_json[poem_number]






