from fastapi import APIRouter, status

from models.posts import Post, PostDocument
from enums import RouterTag


router = APIRouter(
    prefix="/posts",
    tags=[RouterTag.posts],
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Server error"}},
)


@router.get("/", response_model=list[Post])
async def read_posts(skip: int = 0, limit: int = 10):
    return await PostDocument.find({}).skip(skip).limit(limit).to_list()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_data = post.model_dump(exclude_unset=True)
    document = PostDocument(**post_data)
    await PostDocument.save(document)
