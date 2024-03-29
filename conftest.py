import pytest

@pytest.fixture
def collector():
    from main import BooksCollector
    return BooksCollector()