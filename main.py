from src.user_interaction import UserInteraction


def main():
    user_input = input("Введите название вакансии для поиска: ")

    while True:
        users_salary = input("Укажите зарплату, если хотите\n"
                             "увидеть вакансии с указанной зарплатой:\n")
        if users_salary.isdigit():
            break
        print("\nНеверный формат зарплаты. Введите целое число.")

    user = UserInteraction(user_input)

    while True:
        users_city = input("Введите название города:\n").capitalize()
        if users_city.isalpha():
            break
        print("\nНеверный формат города. Введите название с буквами.")

    user.sorted_salary(user.all_vacancy, int(users_salary), users_city)
    user.get_top_vacancies(user.sort_salary)

    user.save_info()

    while True:
        number_vacancy = input('Введите номер топ вакансии\n'
                               ', если вы хотите увидеть больше: ')
        if number_vacancy.isdigit():
            break
        print("\nНеверный формат номера. Введите целое число.")

    print(user.last_info(user.vacancies_list, int(number_vacancy)))


if __name__ == '__main__':
    main()
