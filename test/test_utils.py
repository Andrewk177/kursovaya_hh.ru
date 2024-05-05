import pytest


def test_get_vacancies():
    api = HHRUVacancyAPI()
    result = api.get_vacancies("Python")
    assert isinstance(result, list)
    assert all("name" in job for job in result)


@pytest.fixture
def file_manager():
    return JSONFileManager("test_vacancies.json")


def test_add_and_get_vacancy(file_manager):
    vacancy = Vacancy("Test Job", "http://example.com", {"from": 50000, "to": 70000, "currency": "USD"}, "Test description")
    file_manager.add_vacancy_to_file(vacancy)
    vacancies = file_manager.get_vacancies_from_file()
    assert len(vacancies) > 0
    assert vacancies[0]['title'] == "Test Job"


def test_delete_vacancy(file_manager):
    file_manager.delete_vacancy_from_file("Test Job")
    vacancies = file_manager.get_vacancies_from_file()
    assert all(vacancy['title'] != "Test Job" for vacancy in vacancies)

