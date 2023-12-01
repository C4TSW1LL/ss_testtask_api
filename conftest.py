import pytest
from base_api.yandex_api import YandexApi


@pytest.fixture
def api(get_token, url, path):
    fch = YandexApi(url, path, get_token)
    return fch


@pytest.fixture
def get_token():
    token = '...'
    return token


@pytest.fixture
def url():
    url = 'https://cloud-api.yandex.net/v1/disk/'
    return url

@pytest.fixture
def path():
    path = "resources?path=disk%3A%2F"
    return path