import os

from typing_extensions import BinaryIO

from src.services.file_data import FileData


class SimpleStorage:
    def __init__(self, storage_path: str):
        self.storage_path = storage_path

    def save_file(self, file_data: FileData) -> str:
        full_path = os.path.join(self.storage_path, file_data.relative_path)

        with open(full_path, "wb") as file:
            file_data.write(file_data.file_stream)


    def download_file(self, fileName: str) -> BinaryIO:
        full_path = os.path.join(self.storage_path, fileName)

        return open(full_path, "rb")

