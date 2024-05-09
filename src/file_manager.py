import json
from api import HHRUVacancyAPI
from vacancy import  Vacancy

class JSONFileManager:
    def __init__(self, file_name="vacancies.json"):
        self.file_name = file_name

    def add_vacancy_to_file(self, vacancy):
        with open(self.file_name, "a") as file:
            json.dump(vars(vacancy), file)
            file.write("\n")

    def get_vacancies_from_file(self):
        with open(self.file_name, "r") as file:
            return [json.loads(line) for line in file]

    def delete_vacancy_from_file(self, title):
        with open(self.file_name, "r") as file:
            vacancies = [json.loads(line) for line in file]
        with open(self.file_name, "w") as file:
            for vacancy in vacancies:
                if vacancy['title'] != title:
                    json.dump(vacancy, file)
                    file.write("\n")

def user_interaction():
    api = HHRUVacancyAPI()
    search_query = input("Enter your search query: ")
    vacancies = api.get_vacancies(search_query)

    file_manager = JSONFileManager()
    for vacancy_data in vacancies:
        vacancy = Vacancy(vacancy_data['name'], vacancy_data['alternate_url'], vacancy_data['salary'], vacancy_data['snippet']['requirement'])
        file_manager.add_vacancy_to_file(vacancy)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacancies = sorted(vacancies, key=lambda x: x['salary'], reverse=True)[:top_n]
    for idx, vacancy_data in enumerate(sorted_vacancies, start=1):
        print(f"Вакансия {idx}: {vacancy_data['name']} - Зарплата: {vacancy_data['salary']}")

    keyword = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = file_manager.get_vacancies_from_file()
    for vacancy in filtered_vacancies:
        if any(word in vacancy['description'] for word in keyword):
            print(f"Отфильтрованные вакансии: {vacancy['title']} - Зарплата: {vacancy['salary']}")
