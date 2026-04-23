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

def get_post(post_id: int) -> Optional[Post]:
    return POSTS.get(post_id)
