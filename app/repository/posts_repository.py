from typing import Optional

from app.db.session import SessionLocal
from app.model.post import Post

POSTS: dict[int, Post] = {}
id_counter = 0


def create_post(post: Post) -> Post:
    db = SessionLocal()
    db.add(post)

    db.commit()

    POSTS[post.id] = post
    return post


def update_post(post: Post) -> Post:
    POSTS[post.id] = post
    return post


def get_post(post_id: int) -> Optional[Post]:
    return POSTS.get(post_id)


def delete_post(post_id: int) -> None:
    POSTS.pop(post_id)
