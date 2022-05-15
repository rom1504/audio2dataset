import pytest
from audio2dataset import hello_world


@pytest.mark.parametrize("message", ["hello", "world"])
def test_hello_world(message):
    hello_world(message)
