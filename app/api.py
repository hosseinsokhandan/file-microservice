import uuid
from fastapi import APIRouter, File, UploadFile
import os
from settings import get_settings

settings = get_settings()


router = APIRouter()


@router.post("/{part_id}")
async def upload_file(part_id: int, file: UploadFile = File(...)):
    filename = uuid.uuid4().hex[:10] + file.filename
    upload_to = os.path.join(
        settings.UPLOAD_DIRECTORY, filename
    )

    with open(upload_to, 'wb+') as f:
        content = await file.read()
        f.write(content)
        f.close()

    return {
        "name": file.filename,
        "path": upload_to,
    }
