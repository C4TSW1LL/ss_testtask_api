import requests
from .parser import Parser


class YandexApi:
    def __init__(self, url, path, token):
        self.token = token
        self.url = url + path

    def GET_method(self):
        response = requests.request(method='get', url=self.url, headers=dict(authorization=f'OAuth {self.token}'))
        return response.status_code, response.json()
