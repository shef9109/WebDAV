from fastapi import APIRouter, UploadFile

from src.services.simple_storage import SimpleStorage


def create_download_router(storage: SimpleStorage):
    download_router = APIRouter()

    return download_router
