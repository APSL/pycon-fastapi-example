import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from db.mongodb import mongo_db
from config import settings
from models.posts import PostDocument
from routers import posts

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(posts.router)
app.mount("/static", StaticFiles(directory=settings.static_path), name="static")


@app.on_event("startup")
async def startup_db_client():
    url = f"mongodb+srv://{settings.db_username}:{settings.db_password}@{settings.db_host}/?retryWrites=true&w=majority"
    mongo_db.client = AsyncIOMotorClient(url)
    db = mongo_db.client[settings.db_name]
    await init_beanie(db, document_models=[PostDocument])


@app.on_event("shutdown")
async def shutdown_db_client():
    mongo_db.client.close()


@app.get("/")
async def ping():
    return {"topic": "Hi World!"}
