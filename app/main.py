from fastapi import FastAPI
from api import router
from settings import get_settings
# from tortoise.contrib.fastapi import register_tortoise
from database import TORTOISE_ORM

settings = get_settings()
app = FastAPI(
    docs_url=f"/{settings.SERVICE_NAME}/docs",
    openapi_url=f"/{settings.SERVICE_NAME}/openapi.json"
)


app.include_router(router, prefix=f"/{settings.SERVICE_NAME}")

# register_tortoise(
#     app,
#     config=TORTOISE_ORM,
#     generate_schemas=False,
#     add_exception_handlers=True,
# )
