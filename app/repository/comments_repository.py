from typing import Sequence

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import select, delete

from app.model.comment import Comment

def get_comment(comment_id: int, db: Session) -> Comment:
    return db.execute(select(Comment).where(Comment.id == comment_id)).scalar_one()

def get_comments_by_post(post_id: int, db: Session) -> Sequence[Comment]:
    return db.execute(select(Comment).where(Comment.post_id == post_id)).scalars().all()


def create_comment(comment: Comment, db: Session) -> Comment:
    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def update_comment(comment: Comment, db: Session) -> Comment:
    db.commit()
    db.refresh(comment)

    return comment


def delete_comment(comment_id: int, db: Session) -> None:
    db.execute(delete(Comment).where(Comment.id == comment_id))
    db.commit()
