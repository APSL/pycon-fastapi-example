import logging
from datetime import datetime

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient

from src.db.mongodb import mongo_db, get_db

logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.on_event("startup")
async def startup_db_client():
    url = "mongodb+srv://piton:sHT3blr0TmDWrtb@cluster0.pqy4nj7.mongodb.net/?retryWrites=true&w=majority"
    mongo_db.client = AsyncIOMotorClient(url)


@app.on_event("shutdown")
async def shutdown_db_client():
    mongo_db.client.close()


@app.get("/")
async def ping():
    return {"topic": "Hi World!"}


@app.get("/posts")
async def read_posts(db=Depends(get_db)):
    return await db.posts.find({}, {'_id': 0}).to_list(10)


@app.post("/posts", status_code=201)
async def create_posts(title: str, created_at: datetime, author: str, db=Depends(get_db)):
    db.posts.insert_one({'title': title, 'created_at': created_at, 'author': author})
