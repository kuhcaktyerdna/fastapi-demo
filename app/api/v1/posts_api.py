from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session

from app.db.session import get_db
from app.schemas.posts import CreatePostRequest, PostDTO, UpdatePostRequest
from app.service import posts_service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/", response_model=list[PostDTO])
def get_posts(db: Session = Depends(get_db)) -> list[PostDTO]:
    return posts_service.get_all(db)


@router.get("/{post_id:int}")
def get_post(post_id: int, db: Session = Depends(get_db)) -> PostDTO:
    return posts_service.get_post(post_id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(create_post_request: CreatePostRequest, db: Session = Depends(get_db)) -> PostDTO:
    return posts_service.create_post(create_post_request, db)


@router.put("/{post_id:int}")
def update_post(post_id: int, update_post_request: UpdatePostRequest, db: Session = Depends(get_db)) -> PostDTO:
    return posts_service.update_post(post_id, update_post_request, db)


@router.delete("/{post_id:int}", status_code=status.HTTP_200_OK)
def delete_post(post_id: int, db: Session = Depends(get_db)) -> None:
    posts_service.delete_post(post_id, db)
