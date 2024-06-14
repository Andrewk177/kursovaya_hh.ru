import pytest
from src.compare_vacancies import CompareVacancies


def test_get_top_vacancies():
    compare_obj = CompareVacancies("Software Developer")
    sort_salary = {
        50000: [{"salary": {"to": 90000}}],
        60000: [{"salary": {"to": 100000}}],
        70000: [{"salary": {"to": 110000}}],
    }
    top_vacancies = compare_obj.get_top_vacancies(sort_salary)
    assert 110000 in top_vacancies
    assert len(top_vacancies[110000]) == 1

def test_get_top_vacancies_no_results():
    compare_obj = CompareVacancies("Software Developer")
    sort_salary = {}
    top_vacancies = compare_obj.get_top_vacancies(sort_salary)
    assert top_vacancies == "Vacancy not found"

if __name__ == '__main__':
    pytest.main()
