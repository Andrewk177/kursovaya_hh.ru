from abc import ABC, abstractmethod
import json


class AbstractJSON(ABC):

    @abstractmethod
    def save_vacancies_to_file(self, vacancies, file_path):
        with open(file_path, 'w') as file:
            json.dump(vacancies, file)

    @abstractmethod
    def view_vacancies_from_file(self, file_path):
        with open(file_path, 'r') as file:
            vacancies = json.load(file)
        return vacancies


class JSONHandler(AbstractJSON):

    def delete_vacancies_from_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write("")