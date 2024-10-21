from typing import BinaryIO


class FileData:
    def __init__(self, relative_path: str, file_stream: BinaryIO):
        self.relative_path = relative_path
        self.file_stream = file_stream

