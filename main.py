from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

POSTS = {}
id_counter = 0

class CreatePostRequest(BaseModel):
    title: str
    content: str

@app.post("/posts/")
def create_post(create_post_request: CreatePostRequest):
    global id_counter

    POSTS[id_counter] = create_post_request
    id_counter += 1
    return Response(status_code=201, content=f"post created with id {id_counter - 1}")


@app.get("/posts/{post_id:int}")
def get_post(post_id: int):
    return POSTS[post_id]