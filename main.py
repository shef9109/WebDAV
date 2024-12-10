from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import aiofiles
import os
from starlette.middleware.wsgi import WSGIMiddleware
from wsgidav.wsgidav_app import WsgiDAVApp
from wsgidav.dav_provider import DAVProvider

# Создаем FastAPI приложение
app = FastAPI()
UPLOAD_DIR = "static"

# Убедитесь, что директория для загрузки существует
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()  # читаем файл
        await out_file.write(content)  # записываем файл
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

@app.get("/files/{filename}")
async def get_file(filename: str):
    file_location = f"{UPLOAD_DIR}/{filename}"
    return FileResponse(file_location)

# Настройка WebDAV
wsgi_app = WsgiDAVApp({
    'host': '127.0.0.1',
    'port': 8081,
    'provider_mapping': {
        '/': UPLOAD_DIR,
    },
    'simple_dc': {
        'user_mapping': {
            '*': {
                'user': 'user',
                'password': 'password',
            },
        },
    },
    'verbose': 1,
    'realm': 'My WebDAV Realm',
})

# Оборачиваем WSGI приложение в Starlette middleware
app.mount("/webdav", WSGIMiddleware(wsgi_app))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)