from fastapi import APIRouter
from starlette.responses import Response

from app.schemas.posts import CreatePostRequest, PostDTO
from app.service import posts_service

router = APIRouter(prefix="/api/v1/posts", tags=["posts"])

@router.post("/")
def create_post(create_post_request: CreatePostRequest) -> Response:
    post_dto: PostDTO = posts_service.create_post(create_post_request)
    return Response(status_code=201, content=f"post created with id {post_dto.id}")


@router.get("/{post_id:int}")
def get_post(post_id: int) -> PostDTO:
    return posts_service.get_post(post_id)