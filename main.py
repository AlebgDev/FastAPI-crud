from typing import Union,Text,Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

posts = []

#Post model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text 
    created_at: datetime=datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def save_posts(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get("/posts/{post_id}")
def get_post(post_id : str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    for index,post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"Message": "Post has been deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"]= updatedPost.dict()["title"]
            posts[index]["content"]= updatedPost.dict()["content"]
            posts[index]["author"]= updatedPost.dict()["author"]
            return {"message": "Post has been updated succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")