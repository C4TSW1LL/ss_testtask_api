import requests


class YandexApiClient:
    url = "https://cloud-api.yandex.net/v1/disk/"
    token = "y0_AgAAAAByb1ODAADLWwAAAADzbOpmCEE7bzh2Swq1KU1x5Gl1vooS0gA"

    @staticmethod
    def get_all_files():
        return requests.request(method='get', url=YandexApiClient.url + "resources?path=disk%3A%2F",
                                headers=dict(authorization=f'OAuth {YandexApiClient.token}'))
