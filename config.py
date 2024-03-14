from pydantic import BaseSettings, AnyHttpUrl
from typing import Optional
import pathlib
import os

env_name = os.getenv("ACTIVE_ENVIRONMENT")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")


class Settings(BaseSettings):
    WEBAPP: str
    PORT: int
    SOCKET_PORT: int
    DYNAMODB: str
    DYNAMODB_REGION: str
    LAMBDA_REGION: str
    LOCAL_ENV: bool
    AWS_ACCESS_KEY_ID: str = aws_access_key_id
    AWS_SECRET_ACCESS_KEY: str = aws_secret_access_key
    DB_API: AnyHttpUrl

    class Config:
        env_file = pathlib.Path.joinpath(pathlib.Path(__file__).resolve().parents[0], f"../ocpp-backend/config/{env_name}.env" )


if __name__ == "__main__":
    settings = Settings()
