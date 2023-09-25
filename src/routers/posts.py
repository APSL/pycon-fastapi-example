import logging

from fastapi import APIRouter, HTTPException, status
from fastapi_versioning import version

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


@router.put("/{title}/like", status_code=status.HTTP_200_OK, deprecated=True)
@version(1, 0)
async def like_posts_deprecated(title: str, likes: int = 1) -> int:
    result = await PostDocument.find_one(PostDocument.title == title).inc({str(PostDocument.likes): likes})
    if result.modified_count:
        logger.info(f"Liked++ {title}")
        post = await PostDocument.find_one(PostDocument.title == title)
        return post.likes
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')


@router.put("/{title}/like", status_code=status.HTTP_200_OK)
@version(1, 1)
async def like_posts(title: str):
    result = await PostDocument.find_one(PostDocument.title == title).inc({str(PostDocument.likes): 1})
    if result.modified_count:
        logger.info(f"Liked++ {title}")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
