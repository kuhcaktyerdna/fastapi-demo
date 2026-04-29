from datetime import datetime, timezone

from sqlalchemy.orm.session import Session

from app.exception.business_exceptions import EntityNotFoundException
from app.mapper import comments_mapper
from app.model.comment import Comment
from app.repository import comments_repository, posts_repository
from app.schemas.comments import (
    CreateCommentRequest,
    UpdateCommentRequest,
    CommentDTO
)


def get_comments_by_post(post_id: int, db: Session) -> list[CommentDTO]:
    if not posts_repository.get_post(post_id, db):
        raise EntityNotFoundException(message=f"Comments cannot be found as Post with id {post_id} does not exist")
    return list(map(comments_mapper.entity_to_dto, comments_repository.get_comments_by_post(post_id, db)))


def create_comment(create_comment_request: CreateCommentRequest, db: Session) -> CommentDTO:
    post_id: int = create_comment_request.post_id

    if not posts_repository.get_post(post_id, db):
        raise EntityNotFoundException(message=f"Comment cannot be created as Post with id {post_id} does not exist")

    comment: Comment = Comment()
    comment.post_id = post_id
    comment.content = create_comment_request.content

    return comments_mapper.entity_to_dto(comments_repository.create_comment(comment, db))


def update_comment(comment_id: int, update_comment_request: UpdateCommentRequest, db: Session) -> CommentDTO:
    comment: Comment = comments_repository.get_comment(comment_id, db)
    if comment is None:
        raise EntityNotFoundException(Comment.__name__, comment_id)

    comment.content = update_comment_request.content
    comment.updated_at = datetime.now(timezone.utc)
    comments_repository.update_comment(comment, db)
    return comments_mapper.entity_to_dto(comment)


def delete_comment(comment_id: int, db: Session) -> None:
    comments_repository.delete_comment(comment_id, db)
