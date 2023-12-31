import os
from typing import Any, List, Optional, Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, HttpUrl, PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_MINUTES: int = os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES")
    AUTHENTICATION__ALGORITHM: str = os.getenv("AUTHENTICATION__ALGORITHM")
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_REFRESH_SECRET_KEY: str = os.getenv('JWT_REFRESH_SECRET_KEY')

    SMTP_SERVER: str = os.getenv("SMTP_SERVER")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT"))
    SMTP_USER_NAME: str = os.getenv("SMTP_USER_NAME")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD")

    SERVER_NAME: str = "event finder application"
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1:8000"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://127.0.0.1:3000"]



    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "event finder application"
    # SENTRY_DSN: Optional[HttpUrl] = ""
    #
    # @field_validator("SENTRY_DSN", mode="before")
    # @classmethod
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v
    #
    # POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    # POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    # POSTGRES_SERVER: str = f"{POSTGRES_HOST}:{POSTGRES_PORT}"
    # POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    # POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    # POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    # SQLALCHEMY_DATABASE_URI: Optional[str] = os.getenv("DATABASE_URL")
    #
    # @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    # @classmethod
    # def assemble_db_connection(cls, v: Optional[str], info: FieldValidationInfo) -> Any:
    #     if isinstance(v, str):
    #         return v
    #     postgres_dsn = PostgresDsn.build(
    #         scheme="postgresql",
    #         username=info.data.get("POSTGRES_USER"),
    #         password=info.data.get("POSTGRES_PASSWORD"),
    #         host=info.data.get("POSTGRES_SERVER"),
    #         path=f"{info.data.get('POSTGRES_DB') or ''}",
    #     )
    #     return str(postgres_dsn)
    #
    # class Config:
    #     case_sensitive = True


settings = Settings()
