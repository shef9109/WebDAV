from fastapi import APIRouter

load_router = APIRouter()

@load_router.get("/{file_id}")
async def sharing_file(file_id: str):
    return "NOT IMPLEMENTED"