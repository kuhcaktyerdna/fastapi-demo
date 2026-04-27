from datetime import datetime, timezone

from sqlalchemy.orm.session import Session

from app.exception.business_exceptions import EntityNotFoundException
from app.mapper import post_mapper
from app.model.post import Post
from app.repository import posts_repository
from app.schemas.posts import CreatePostRequest, PostDTO, UpdatePostRequest


def get_all(db: Session) -> list[PostDTO]:
    return list(map(post_mapper.entity_to_dto, posts_repository.get_all_posts(db)))


def get_post(post_id: int, db: Session) -> PostDTO:
    post = posts_repository.get_post(post_id, db)
    if post is None:
        raise EntityNotFoundException(Post.__name__, post_id)

    return post_mapper.entity_to_dto(post)


def create_post(create_post_request: CreatePostRequest, db: Session) -> PostDTO:
    post: Post = Post()
    post.title = create_post_request.title
    post.content = create_post_request.content

    return post_mapper.entity_to_dto(posts_repository.create_post(post, db))


def update_post(post_id: int, update_post_request: UpdatePostRequest, db: Session) -> PostDTO:
    post = posts_repository.get_post(post_id, db)
    if post is None:
        raise EntityNotFoundException(Post.__name__, post_id)

    post.title = update_post_request.title
    post.content = update_post_request.content
    post.updated_at = datetime.now(timezone.utc)
    posts_repository.update_post(post, db)
    return post_mapper.entity_to_dto(post)


def delete_post(post_id: int, db: Session) -> None:
    posts_repository.delete_post(post_id, db)
