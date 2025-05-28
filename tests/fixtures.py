import pytest
from csvreader import CsvReader


@pytest.fixture(scope="function")
def reader():
    "create and return reader instance"
    reader = CsvReader()
    yield reader
