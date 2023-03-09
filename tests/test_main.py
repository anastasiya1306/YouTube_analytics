from main import Channel
import pytest


@pytest.fixture
def ch1():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture
def ch2():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')


def test_str(ch1):
    assert ch1.__str__() == 'Youtube-канал: вДудь'

def test_add(ch1, ch2):
    assert ch1.__add__(ch2) == 14000000

def test_lt(ch1, ch2):
    assert ch1.__lt__(ch2) is False
