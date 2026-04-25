from fastapi import APIRouter, status

from app.schemas.posts import CreatePostRequest, PostDTO, UpdatePostRequest
from app.service import posts_service

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(create_post_request: CreatePostRequest) -> PostDTO:
    return posts_service.create_post(create_post_request)

@router.get("/{post_id:int}")
def get_post(post_id: int) -> PostDTO:
    return posts_service.get_post(post_id)

@router.put("/{post_id:int}")
def update_post(post_id: int, update_post_request: UpdatePostRequest) -> PostDTO:
    return posts_service.update_post(post_id, update_post_request)

@router.delete("/{post_id:int}", status_code=status.HTTP_200_OK)
def delete_post(post_id: int) -> None:
    posts_service.delete_post(post_id)