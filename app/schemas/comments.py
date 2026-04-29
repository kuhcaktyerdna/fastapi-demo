from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class CreateCommentRequest(BaseModel):
    post_id: int
    content: str = Field(..., min_length=1)


class UpdateCommentRequest(BaseModel):
    content: str = Field(..., min_length=1)


class CommentDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    post_id: int
    created_at: datetime
    updated_at: datetime | None = None
