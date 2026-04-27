from typing import Optional, Sequence

from sqlalchemy.future import select
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import delete

from app.model.post import Post


def get_all_posts(db: Session) -> Sequence[Post]:
    return db.execute(select(Post)).scalars().all()


def get_post(post_id: int, db: Session) -> Optional[Post]:
    return db.execute(select(Post).where(Post.id == post_id)).scalar_one()


def create_post(post: Post, db: Session) -> Post:
    db.add(post)
    db.commit()
    db.refresh(post)

    return post


def update_post(post: Post, db: Session) -> Post:
    db.commit()
    db.refresh(post)
    return post


def delete_post(post_id: int, db: Session) -> None:
    db.execute(delete(Post).where(Post.id == post_id))
    db.commit()
