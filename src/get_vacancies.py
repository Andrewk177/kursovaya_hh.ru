import json
from typing import Any
import requests
from config import DATA
from src.abstract_hh import AbstractJSON
from src.abstract_hh import JSONHandler


class GetVacancies(AbstractJSON):
    all = []

    def __init__(self, name_vacancy: str):
        self.name_vacancy: str = name_vacancy
        self.message = "Vacancies found"
        self.all_vacancy = self.get_vacancy_from_api()

    def __repr__(self):
        return f"{self.all_vacancy}"

    def get_vacancy_from_api(self) -> str | Any:
        """
        Получает достоверную информацию о вакансиях для пользователя
        """

        if isinstance(self.name_vacancy, str):
            keys_response = {'text': f'NAME:{self.name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            return json.loads(info.text)['items']
        else:
            self.message = "Vacancy not found"
            return self.message

    def save_info(self) -> str or list:
        """
        Создает json файл с информацией о вакансиях
        """

        if len(self.all_vacancy) == 0:
            self.message = "Vacancy not found"
            return self.message
        else:
            with open(DATA, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
            return self.all_vacancy


class HeadHunterAPI(JSONHandler):
    def save_vacancies_to_file(self, vacancies, file_path):
        super().save_vacancies_to_file(vacancies, file_path)

    def view_vacancies_from_file(self, file_path):
        return super().view_vacancies_from_file(file_path)