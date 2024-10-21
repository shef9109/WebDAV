from fastapi import APIRouter, UploadFile

from src.services.file_data import FileData
from src.services.simple_storage import SimpleStorage


def create_upload_router(storage: SimpleStorage):
  upload_router = APIRouter()

  @upload_router.post("/")
  def upload_file(file: UploadFile):
    storage.save_file(FileData(file.filename, file.file))

  return upload_router