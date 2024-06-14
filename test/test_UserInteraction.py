import pytest
from src.user_interaction import UserInteraction


@pytest.fixture
def mocked_top_salary():
    return {
        1: [
            {'name': 'Software Engineer', 'salary': {'from': 60000, 'to': 80000}, 'area': {'name': 'San Francisco'}, 'alternate_url': 'example.com'}
        ]
    }


def test_make_info(capfd, mocked_top_salary):
    user_interaction = UserInteraction("Software Developer")
    user_interaction.make_info(mocked_top_salary)

    captured = capfd.readouterr()
    output = captured.out

    assert "Top salary" in output
    assert "1. Top salary 1 - count 1" in output
    assert "Name of vacancy: Software Engineer" in output
    assert "Salary from: 60000" in output
    assert "Salary to: 80000" in output
    assert "City: San Francisco" in output
    assert "URL: example.com" in output


def test_str():
    user_interaction = UserInteraction("Software Developer")
    output = user_interaction.__str__()
    expected_output = (
        f"Name of vacancy for search: Software Developer\nCount vacancies: 100\nStatus: Vacancies found"
    )
    assert output == expected_output

if __name__ == '__main__':
    pytest.main()
