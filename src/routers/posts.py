import logging
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi_versioning import version
from pymongo.errors import DuplicateKeyError

from models.posts import PostIn, Post, PostOut


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Server error"}},
)


@router.get("/", response_model=List[PostOut])
async def read_posts():
    pass


def simple_post(title: str, user: str):
    return {"title": title, "user": user}


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_409_CONFLICT: {"description": "Title is duplicated"}},
)
async def create_posts(post: dict = Depends(simple_post)):
    pass


@router.delete(
    "/{title}",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_409_CONFLICT: {"description": "Not exists"}},
)
async def delete_posts(title: str):
    pass


@router.put("/{title}/like", status_code=status.HTTP_200_OK)
async def like_posts(title: str, likes: int) -> int:
    pass
