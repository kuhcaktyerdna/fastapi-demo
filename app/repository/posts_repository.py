from typing import Optional

from app.model.post import Post

POSTS: dict[int, Post] = {}
id_counter = 0

def create_post(post: Post) -> Post:
    global id_counter

    post.id = id_counter
    POSTS[id_counter] = post
    id_counter += 1
    return post


def update_post(post: Post) -> Post:
    POSTS[post.id] = post
    return post


def get_post(post_id: int) -> Optional[Post]:
    return POSTS.get(post_id)


def delete_post(post_id: int) -> None:
    POSTS.pop(post_id)
