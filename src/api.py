from abc import ABC, abstractmethod
import requests

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str) -> list:
        pass

class HHRUVacancyAPI(AbstractVacancyAPI):
    _url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query: str) -> list:
        params = {"text": search_query, "area": "1", "per_page": 50}
        response = requests.get(self._url, params=params)
        return response.json().get("items", []) if response.status_code == 200 else []
