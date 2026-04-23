from fastapi import APIRouter
from starlette.responses import Response

from app.schemas.posts import CreatePostRequest

router = APIRouter(prefix="/api/v1/posts", tags=["posts"])

POSTS = {}
id_counter = 0

@router.post("/")
def create_post(create_post_request: CreatePostRequest):
    global id_counter

    POSTS[id_counter] = create_post_request
    id_counter += 1
    return Response(status_code=201, content=f"post created with id {id_counter - 1}")


@router.get("/{post_id:int}")
def get_post(post_id: int):
    return POSTS[post_id]