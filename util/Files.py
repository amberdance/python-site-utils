import os.path
import pathlib
import shutil
from pathlib import Path
from exception.UnsupportedOperationException import UnsupportedOperationException


class Files:

    def __init__(self) -> None:
        raise UnsupportedOperationException()

    @staticmethod
    def path(file: str) -> Path:
        return pathlib.Path(file).absolute()

    @staticmethod
    def backup_file(file: str, backup_file_name: str) -> any:
        return shutil.copy(file, os.path.join(Files.path(file).parent,
                                              file + "." + backup_file_name + Files.get_file_extension(file)))

    @staticmethod
    def get_file_extension(file: str) -> str:
        return pathlib.Path(file).suffix

    @staticmethod
    def get_root_directory() -> str:
        return os.getcwd()
