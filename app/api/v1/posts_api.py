from fastapi import APIRouter, status

from app.schemas.posts import CreatePostRequest, PostDTO
from app.service import posts_service

router = APIRouter(prefix="/api/v1/posts", tags=["posts"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(create_post_request: CreatePostRequest) -> PostDTO:
    return posts_service.create_post(create_post_request)


@router.get("/{post_id:int}")
def get_post(post_id: int) -> PostDTO:
    return posts_service.get_post(post_id)