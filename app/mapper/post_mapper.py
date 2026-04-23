from app.model.post import Post
from app.schemas.posts import PostDTO


def entity_to_dto(post: Post) -> PostDTO:
    return PostDTO(
        id=post.id,
        title=post.title,
        content=post.content
    )
