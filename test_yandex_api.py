from base_api.parser import Parser
from base_api.YandexApiClient import YandexApiClient


class TestYandexApi:

    def test_get_all_file_name(self):
        response = YandexApiClient.get_all_files()
        names = Parser.get_all_name(response.json())

        assert response.status_code == 200
        assert names.get("name") != [""]
