from fastapi import FastAPI, Path
from pydantic import BaseModel
from inventoryb import *
import typing
import random as r

class Poem(BaseModel):
    style: str
    author: str
    title: str
    content: str


# check on the actual inventory
print(poem_json)
# set up FastAPI and the actual API
app = FastAPI()

# /home endpoint
@app.get("/")
def home() -> typing.Dict[str, str]:
    return {"Data":"Test"}

# /about endpoint
@app.get("/about")
def about() -> typing.Dict[str, str]:
    return {"name": "300TPAPI", "info": "An API for Chinese philosophy quotes made using FastAPI.", "author": "Necloremius",
            "Date created": "03/06/2022"}



# /get-poem: item based on ID endpoint
@app.get("/get-poem/{poem_number}") # path parameter
def get_item(poem_number: int = Path(None, description="Number of poem that you would like to request data for.", gt=0, lt=321)):
    return poem_json[poem_number]


# /rand-poem: random poem
@app.get("/rand-poem")
def rand_poem() -> None:
    x = r.randint(1, 321)
    return poem_json[x]












