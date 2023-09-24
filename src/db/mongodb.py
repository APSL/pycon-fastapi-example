from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoDB:
    client: AsyncIOMotorClient = None


mongo_db = MongoDB()


def get_db() -> AsyncIOMotorDatabase:
    """Get NOSQL db"""
    return mongo_db.client["pycon"]
