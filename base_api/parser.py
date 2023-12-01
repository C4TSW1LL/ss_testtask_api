import json


class Parser:
    """
    Метод get_all_name принимает в себя ответ в формате json
    Выводит в консоль список имен всех файлов и папок на диске в словарь
    Создает файл для дальнейшего парсинга
    """

    @staticmethod
    def get_all_name(response):
        data = {"name": []}
        for i in response['_embedded']['items']:
            data["name"].append(i["name"])

        with open('all_file_in_disk.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("\n", data)
        return data
