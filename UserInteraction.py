from CompareVacancies import CompareVacancies

class UserInteraction(CompareVacancies):
    def __init__(self, name_vacancy):
        super().__init__(name_vacancy)
        self.get_vacancy_from_api()

    def __str__(self):
        self.message = "Vacancy not found" if len(self.all_vacancy) == 0 else self.message
        return (f"Name of vacancy for search: {self.name_vacancy}\n"
                f"Count vacancies: {len(self.all_vacancy)}\n"
                f"Status: {self.message}")

    def make_info(self, top_salary: dict) -> None:
        """
        Редактирует список вакансий для пользователя и выводит на экран
        """
        print("Top salary:")
        count = 1
        for top, vacancies in top_salary.items():
            print(f"{count}. Top salary {top} - count {len(vacancies)}", end='\n')
            for value in vacancies:
                print(f"Name of vacancy: {value['name']}")
                print(f"Salary from: {value['salary']['from']}")
                print(f"Salary to: {value['salary']['to']}")
                print(f"City: {value['area']['name']}")
                print(f"URL: {value['alternate_url']}\n")
            count += 1

    @staticmethod
    def last_info(top_salary: dict, number_of_vacancies: int):
        """
        Выводит информацию про топовые вакансии
        """
        print()
        info = []
        for params_vacancy in top_salary[int(number_of_vacancies)]:
            for key, val in params_vacancy.items():
                info.append("{0}: {1}".format(key, val))
        return '\n'.join(info)
