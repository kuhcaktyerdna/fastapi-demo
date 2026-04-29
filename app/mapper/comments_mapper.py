from app.model.comment import Comment
from app.schemas.comments import CommentDTO


def entity_to_dto(post: Comment) -> CommentDTO:
    return CommentDTO.model_validate(post)
