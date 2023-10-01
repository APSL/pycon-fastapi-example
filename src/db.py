from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from config import settings


class MongoManager:
    client: AsyncIOMotorClient

    @property
    def db(self) -> AsyncIOMotorDatabase:
        return self.client[settings.db_name]


mongodb = MongoManager()


def init_db(app: FastAPI, document_models: list):
    @app.on_event("startup")
    async def startup_db_client():
        extra = "retryWrites=true&w=majority"
        url = f"mongodb+srv://{settings.db_username}:{settings.db_password}@{settings.db_host}/?{extra}"
        client = AsyncIOMotorClient(url)
        mongodb.client = client
        await init_beanie(database=mongodb.db, document_models=document_models)

    @app.on_event("shutdown")
    async def shutdown_db_client():
        mongodb.client.close()
