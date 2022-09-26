import pytest
import errno
import os

from file_handler import *


class TestFile:
    def __init__(self, data: str):
        self.data = data

    def read(self) -> str:
        return self.data


class MyFileSystem:
    EXISTING_FILES = {"test": TestFile("testtesttest"), "test2": TestFile("test2test2test2")}
    NON_EXISTING_FILES = ["test3", "test4"]

    @staticmethod
    def open(file_name: str, method: str):

        if method == "r":
            if file_name not in MyFileSystem.EXISTING_FILES.keys():
                print(f"MyFileSystem not found")
                raise Exception()
            return MyFileSystem.EXISTING_FILES[file_name]
        else:
            return TestFile("")


class MyOpen(object):

    def __init__(self, path: str, method: str):
        print(f"\nMy open {path}")
        self.file_obj = MyFileSystem.open(path, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exception_type, value, traceback):
        print("exit function")
        print(exception_type)
        return exception_type


@pytest.mark.parametrize("file_name", MyFileSystem.EXISTING_FILES.keys())
def test_should_return_file_content_for_existing_file(file_name, mocker):
    file_handler = FileHandler(file_name)
    mocker.patch('file_handler.open', MyOpen)
    assert file_handler.read_from_file() == MyFileSystem.EXISTING_FILES[file_name].data


@pytest.mark.parametrize("file_name", MyFileSystem.NON_EXISTING_FILES)
def test_should_raise_error_file_not_found_for_nonexisting_file(file_name, mocker):
    file_handler = FileHandler(file_name)
    mocker.patch('file_handler.open', MyOpen)
    with pytest.raises(Exception):
        file_handler.read_from_file()
