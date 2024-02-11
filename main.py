from typing import Union,Text
from pydantic import BaseModel
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

posts = []

#Post model
class Post(BaseModel):
    id: str
    title: str
    author: str
    content: Text 
    created_at: datetime=datetime.now()
    published_at: datetime


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}