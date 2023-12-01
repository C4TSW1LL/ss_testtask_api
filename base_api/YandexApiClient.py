import requests


class YandexApiClient:
    url = "https://cloud-api.yandex.net/v1/disk/"
    token = "..."

    @staticmethod
    def get_all_files():
        return requests.request(method='get', url=YandexApiClient.url + "resources?path=disk%3A%2F",
                                headers=dict(authorization=f'OAuth {YandexApiClient.token}'))
