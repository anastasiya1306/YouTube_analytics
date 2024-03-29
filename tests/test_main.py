from main import Channel, Video, PLVideo, PlayList
import pytest


@pytest.fixture
def ch1():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture
def ch2():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')


@pytest.fixture
def pl():
    return PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


@pytest.fixture
def video1():
    return Video('9lO06Zxhu88')

@pytest.fixture
def video2():
    return PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')

def test_str(ch1):
    assert ch1.__str__() == 'Youtube-канал: вДудь'

def test_add(ch1, ch2):
    assert ch1.__add__(ch2) == 14010000

def test_lt(ch1, ch2):
    assert ch1.__lt__(ch2) is False


def test_str(video1):
    assert video1.__str__() == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_str(video2):
    assert video2.__str__() == 'Пушкин: наше все? (Литература)'


def test_playlist(pl):
    assert pl.title == 'Редакция. АнтиТревел'
    assert pl.url == 'https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
    duration = pl.total_duration
    assert str(duration) == '3:41:01'
    assert str(type(duration)) == "<class 'datetime.timedelta'>"
    assert str(duration.total_seconds()) == '13261.0'
    assert pl.show_best_video() == 'https://www.youtube.com/watch?v=9Bv2zltQKQA'


def test_video():
    broken_video = Video('broken_video_id')
    assert broken_video.video_title == None
    assert broken_video.like_count == None