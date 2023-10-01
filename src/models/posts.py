from datetime import datetime

from pydantic import BaseModel, Field
from beanie import Document, Indexed


class PostBase(BaseModel):
    """Common fields for posts"""

    title: Indexed(str, unique=True)
    author: str
    likes: int = 0
    created_at: datetime = Field(default_factory=datetime.now)


class PostIn(PostBase):
    """maybe sensible fields, this data is received from the API clients"""

    author: str = Field(..., alias='user')


class Post(PostBase, Document):
    """Stored post fields on collections"""

    pass


class PostOut(PostBase):
    """non-sensible fields, this data is send to the API clients"""

    pass
