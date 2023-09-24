import os

from pydantic_settings import BaseSettings


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))


class Settings(BaseSettings):
    db_host: str
    db_name: str
    db_username: str
    db_password: str

    logging_file_path: str = os.path.join(PROJECT_PATH, "config.d/logging.conf")
    static_path: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")

    class Config:
        env_file = "config.d/.env", "config.d/.secrets"


settings: Settings = Settings()
