import requests


class ApiClient():
    url = "https://cloud-api.yandex.net/v1/disk/"
    token = 'y0_AgAAAAByb1ODAADLWwAAAADzbOpmCEE7bzh2Swq1KU1x5Gl1vooS0gA'

    def get_all_files(self):
        response = requests.request(method='get', url=self.url + "resources?path=disk%3A%2F", headers=dict(authorization=f'OAuth {self.token}'))
        return response.status_code, response.json()
