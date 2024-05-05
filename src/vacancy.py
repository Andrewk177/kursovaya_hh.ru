class Vacancy:
    __slots__ = ['title', 'link', 'salary', 'description']
    def __init__(self, title: str, link: str, salary: dict, description: str):
        self.title = title
        self.link = link
        self.salary = self.parse_salary(salary)
        self.description = description

    @staticmethod
    def parse_salary(salary_data: dict) -> str:
        if not salary_data:
            return "Salary not specified"
        return f"{salary_data.get('from', 'N/A')} - {salary_data.get('to', 'N/A')} {salary_data.get('currency', '')}"

