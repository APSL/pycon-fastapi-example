import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/")
async def ping():
    return {"topic": "Hi World!"}
