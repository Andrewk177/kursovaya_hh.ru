import json
import pytest
from GetVacancies import GetVacancies

def test_get_vacancy_from_api_valid_response():
    get_vacancies = GetVacancies("Software Developer")
    all_vacancy = get_vacancies.get_vacancy_from_api()
    assert isinstance(all_vacancy, list)
    assert len(all_vacancy) > 0

def test_get_vacancy_from_api_invalid_response():
    get_vacancies = GetVacancies(123)
    message = get_vacancies.get_vacancy_from_api()
    assert message == "Vacancy not found"

def save_info(self) -> str or list:
    if len(self.all_vacancy) == 0:
        self.message = "Vacancy not found"
        return self.message
    else:
        with open(data, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
        return self.all_vacancy


if __name__ == '__main__':
    pytest.main()
