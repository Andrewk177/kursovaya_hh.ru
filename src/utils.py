import requests
import json
from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HHRUVacancyAPI(AbstractVacancyAPI):
    def connect_to_api(self):
        pass

    def get_vacancies(self, search_query):
        url = f"https://api.hh.ru/vacancies"
        params = {"text": search_query, "area": "1"}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            return []


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary


class FileManager(ABC):
    @abstractmethod
    def add_vacancy_to_file(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_from_file(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy_from_file(self, criteria):
        pass


class JSONFileManager(FileManager):
    def add_vacancy_to_file(self, vacancy):
        with open("vacancies.json", "a") as file:
            json.dump(vars(vacancy), file)
            file.write("\n")

    def get_vacancies_from_file(self, criteria):
        with open("vacancies.json", "r") as file:
            vacancies = [json.loads(line) for line in file]
            filtered_vacancies = [vacancy for vacancy in vacancies if criteria in vacancy.get("description", "")]
            return filtered_vacancies

    def delete_vacancy_from_file(self, criteria):
        with open("vacancies.json", "r") as file:
            vacancies = [json.loads(line) for line in file]
        with open("vacancies.json", "w") as file:
            for vacancy in vacancies:
                if criteria not in vacancy.get("title", ""):
                    json.dump(vacancy, file)
                    file.write("\n")


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    api = HHRUVacancyAPI()
    vacancies = api.get_vacancies(search_query)

    file_manager = JSONFileManager()
    for vacancy_data in vacancies:
        vacancy = Vacancy(vacancy_data.get("имя"), vacancy_data.get("alternate_url"), vacancy_data.get("зарплата"),
                          vacancy_data.get("описание"))
        file_manager.add_vacancy_to_file(vacancy)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacancies = sorted(vacancies, key=lambda x: x.get("зарплата", 0), reverse=True)[:top_n]
    for idx, vacancy_data in enumerate(sorted_vacancies, start=1):
        print(f"Вакансия {idx}: {vacancy_data.get('имя')} - Зарплата: {vacancy_data.get('зарплата')}")

    keyword = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = file_manager.get_vacancies_from_file(keyword)
    for vacancy in filtered_vacancies:
        print(f"Отфильтрованные вакансии: {vacancy.get('название')} - Зарплата: {vacancy.get('зарплата')}")

