from datetime import datetime

class Post:
    id: int
    title: str
    content: str
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
