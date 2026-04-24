from app.exception.business_exceptions import EntityNotFoundException
from app.mapper import post_mapper
from app.model.post import Post
from app.repository import posts_repository
from app.schemas.posts import CreatePostRequest, PostDTO


def create_post(create_post_request: CreatePostRequest) -> PostDTO:
    post: Post = Post()
    post.title = create_post_request.title
    post.content = create_post_request.content

    return post_mapper.entity_to_dto(posts_repository.create_post(post))

def get_post(post_id: int) -> PostDTO:
    post = posts_repository.get_post(post_id)
    if post is None:
        raise EntityNotFoundException(Post.__name__, post_id)

    return post_mapper.entity_to_dto(post)
