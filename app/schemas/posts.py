from datetime import datetime

from pydantic import BaseModel, Field


class CreatePostRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)


class UpdatePostRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)


class PostDTO(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime | None = None
