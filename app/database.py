import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import get_settings

settings = get_settings()

TORTOISE_ORM: dict = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": settings.MODELS,
            "default_connection": "default",
        },
    },
}
