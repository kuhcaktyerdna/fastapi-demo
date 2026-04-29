from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.db.session import get_db
from app.schemas.comments import (
    CommentDTO,
    CreateCommentRequest,
    UpdateCommentRequest
)
from app.service import comments_service

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("/{post_id:int}")
def get_comments(post_id: int, db: Session = Depends(get_db)) -> list[CommentDTO]:
    return comments_service.get_comments_by_post(post_id, db)


@router.post("/", status_code=201)
def create_comment(create_comment_request: CreateCommentRequest, db: Session = Depends(get_db)) -> CommentDTO:
    return comments_service.create_comment(create_comment_request, db)


@router.put("/{comment_id:int}")
def update_comment(comment_id: int, update_comment_request: UpdateCommentRequest, db: Session = Depends(get_db)) -> CommentDTO:
    return comments_service.update_comment(comment_id, update_comment_request, db)


@router.delete("/{comment_id:int}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)) -> None:
    comments_service.delete_comment(comment_id, db)