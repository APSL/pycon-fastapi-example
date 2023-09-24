from datetime import datetime

from pydantic import BaseModel, Field
from beanie import Document, Indexed


class Post(BaseModel):
    title: Indexed(str)
    author: str
    created_at: datetime = Field(default_factory=datetime.now)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Mí primer post",
                    "author": "Yop!",
                }
            ]
        }
    }


class PostDocument(Post, Document):
    class Config:
        populate_by_name = True

    class Settings:
        name = "posts"
