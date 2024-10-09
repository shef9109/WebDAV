import uvicorn
from fastapi import FastAPI

from routing import upload_router
from routing import load_router

app : FastAPI = FastAPI()

app.include_router(load_router)
app.include_router(upload_router)

if (__name__ == "__main__"):
    uvicorn.run(app, host="localhost", port=8000)