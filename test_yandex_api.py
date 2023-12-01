from base_api.parser import Parser
from conftest import ApiClient


class TestYandexApi:

    def test_get_all_file_name(self):
        api = ApiClient()
        status_code, response = api.get_all_files()
        names = Parser.get_all_name(response)

        assert status_code == 200
        assert names != {}
