from fastapi import APIRouter

upload_router = APIRouter()

@upload_router.post("/upload")
async def get_file():
    return "NOT IMPLEMENTED"