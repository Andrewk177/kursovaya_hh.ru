from collections import defaultdict
from src.compare_vacancies import CompareVacancies
from src.abstract_hh import JSONHandler
import json


class UserInteraction(JSONHandler, CompareVacancies):
    def __init__(self, name_vacancy):
        super().__init__(name_vacancy)
        self.all_vacancy = self.get_vacancy_from_api()
        self.vacancies_list = {}


    def sorted_salary(self, list_all: list, salary: int, city: str) -> dict:
        """
        Генерирует словарь с необходимой зарплатой и списком вакансий
        """
        sort_salary = defaultdict(list)
        for vacancy in list_all:
            if vacancy.get("salary") is not None and vacancy["salary"].get("from") is not None:
                if vacancy.get("area") and vacancy["area"].get("name") == city:
                    if vacancy["salary"]["from"] >= salary:
                        sort_salary[vacancy["salary"]["from"]].append(vacancy)
        return sort_salary

    def save_vacancies_to_file(self, vacancies, file_path):
        with open(file_path, 'w') as file:
            json.dump(vacancies, file)

    def view_vacancies_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def last_info(top_salary: dict, number_of_vacancies: int):
        print()
        info = []
        for params_vacancy in top_salary.get(int(number_of_vacancies), []):
            for key, val in params_vacancy.items():
                info.append(f"{key}: {val}")
        return '\n'.join(info)
