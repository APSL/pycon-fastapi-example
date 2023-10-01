import logging.config

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi_versioning import VersionedFastAPI

from db import init_db
from config import settings
from models.posts import Post
from routers import posts

logger = logging.getLogger(__name__)
logging.config.fileConfig(settings.logging_file_path, disable_existing_loggers=False)

app = FastAPI(title=settings.app_name)

# routers
app.include_router(posts.router)

# version
app = VersionedFastAPI(app, enable_latest=True, version_format="{major}.{minor}", prefix_format="/v{major}-{minor}")

# static files
app.mount("/static", StaticFiles(directory=settings.static_path), name="static")

# initialize beanie with all documents
init_db(app, [Post])


@app.get("/ping")
async def ping() -> str:
    logger.info("Pong!")
    return "pong"


@app.get('/favicon.ico', include_in_schema=False)
async def favicon() -> FileResponse:
    """Gets favicon of app"""
    return FileResponse(settings.favicon_path)
