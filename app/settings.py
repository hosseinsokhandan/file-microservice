from functools import lru_cache
from pydantic import BaseSettings, Field, PostgresDsn, validator
from typing import Optional, Any, Dict, List
import os


class Settings(BaseSettings):
    DOMAIN: str
    SERVICE_NAME: str
    UPLOAD_DIRECTORY = os.path.join(os.path.dirname(os.getcwd()), "static")

    DB_SCHEME: str = Field(default="postgres")
    DB_HOST: str = Field(default="postgres")
    DB_PORT: str = Field(default="5432")
    DB_NAME: str = Field(default="file")
    DB_USER: str = Field(default="file")
    DB_PASSWD: str = Field(default="123456")
    DATABASE_URL: Optional[PostgresDsn] = None

    MODELS: List = [
        "models",
        # "models.Part",
        "aerich.models",  # aerich
    ]

    @ validator("DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme=values["DB_SCHEME"],
            user=values["DB_USER"],
            password=values["DB_PASSWD"],
            host=values["DB_HOST"],
            port=values["DB_PORT"],
            path=f"/{values['DB_NAME']}",
        )

    class Config:
        case_sensitive: bool = True
        env_file: str = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
