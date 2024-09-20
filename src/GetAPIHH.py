import json

import requests

from src.AbstractGetApiHh import AbstractGetApiHh


class GetApiHh(AbstractGetApiHh):

    def __init__(self):
        self.all_vacancy = []

    def __repr__(self):
        return f"{self.all_vacancy}"

    def get_vacancy_from_api(self, name_vacancy) -> list:
        """Get valid info about vacancies for user"""

        if name_vacancy.isalpha():
            keys_response = {'text': f'NAME:{name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            self.all_vacancy = json.loads(info.text)['items']
            return self.all_vacancy
        else:
            return "Vacancy not found"