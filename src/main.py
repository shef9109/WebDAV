import uvicorn
from fastapi import FastAPI

from routing import create_upload_router
from routing import create_download_router
from config import storage_path

from src.services.simple_storage import SimpleStorage

storage =     SimpleStorage(storage_path)

upload_router = create_upload_router(
    storage
)

download_router = create_download_router(
    storage
)

app : FastAPI = FastAPI()

app.include_router(download_router)
app.include_router(upload_router)

if (__name__ == "__main__"):
    uvicorn.run(app, host="localhost", port=8000)