import logging

from fastapi import APIRouter, status

from models.posts import Post, PostDocument
from enums import RouterTag


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/posts",
    tags=[RouterTag.posts],
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Server error"}},
)


@router.get("/", response_model=list[Post])
async def read_posts(skip: int = 0, limit: int = 10):
    results = await PostDocument.find({}).skip(skip).limit(limit).to_list()
    logger.info(f"Retrieve {len(results)} posts")
    return results


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_data = post.model_dump(exclude_unset=True)
    document = PostDocument(**post_data)
    await PostDocument.save(document)
    post_data = document.model_dump(exclude_unset=True)
    logger.info(f"New post created: {post_data}")
