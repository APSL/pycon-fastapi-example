import logging
from datetime import datetime

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from beanie import Document, Indexed, init_beanie

from src.db.mongodb import mongo_db

logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")


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
        allow_population_by_field_name = True

    class Settings:
        name = "posts"


@app.on_event("startup")
async def startup_db_client():
    url = "mongodb+srv://piton:sHT3blr0TmDWrtb@cluster0.pqy4nj7.mongodb.net/?retryWrites=true&w=majority"
    mongo_db.client = AsyncIOMotorClient(url)
    db = mongo_db.client["pycon"]
    await init_beanie(db, document_models=[PostDocument])


@app.on_event("shutdown")
async def shutdown_db_client():
    mongo_db.client.close()


@app.get("/")
async def ping():
    return {"topic": "Hi World!"}


@app.get("/posts", response_model=list[Post])
async def read_posts():
    return await PostDocument.find({}).to_list(10)


@app.post("/posts", status_code=201)
async def create_posts(post: Post):
    post_data = post.model_dump(exclude_unset=True)
    document = PostDocument(**post_data)
    await PostDocument.save(document)
