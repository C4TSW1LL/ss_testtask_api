from base_api.parser import  Parser


class TestYandexApi:

    def test_get_all_file_name(self, api, url):
        status_code, response = api.GET_method()
        names = Parser.get_all_name(response)

        assert status_code == 200
        assert names != {}
