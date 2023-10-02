from src.super_job_api import SuperjobAPI
from src.head_hunter_api import HeadHunterAPI



def user_interaction():
    flag = True
    while flag == True:
        print("Выберите пункт меню:")
        print("1.Искать вакансии на HH.ru")
        print("2.Искать вакансии на SuperJob.ru")
        print("3.Выход")
        user_input = input("Ваш выбор: ")
        if user_input == '1':
            user_input = input("Введите ключевое слово для поиска вакансии: ")
            user_vacancy_search = HeadHunterAPI()
            user_vacancy_search.params['text'] = user_input
            while True:
                user_input = input("\nВведите минимальную зарплату: \nВаш выбор: ")
                if user_input.isdigit() == True:
                    user_vacancy_search.params['salary_from'] = int(user_input)
                    break
                else:
                    print("Неверный ввод")
            while True:
                user_input = input('Введите количество вакансий для поиска(Максимум 30): \nВаш выбор: ')
                if user_input.isdigit() == True and int(user_input) < 31:
                    user_vacancy_search.params['per_page'] = int(user_input)
                    user_vacancy_search.get_vacancies()
                    user_vacancy_search.print_vacancies()
                    break
                else:
                    print("Неверный ввод")
            while True:
                user_input = input("\nЖелаете удалить какую-либо вакансию? (y/n)")
                if user_input == 'y':
                    user_input = input("Введите номер вакансии для удаления: ")
                    if user_input.isdigit() == True:
                        user_vacancy_search.delete_vacancy(int(user_input))
                        user_vacancy_search.print_vacancies()
                        continue
                    else:
                        print("Неверный ввод")
                else:
                    break


            user_input = input("\nЖелаете продолжить поиск вакансий? (y/n)")
            if user_input == 'y':
                continue
            else:
                flag = False


        elif user_input == '2':
            user_input = input("Введите ключевое слово для поиска вакансии: ")
            user_vacancy_search = SuperjobAPI()
            user_vacancy_search.params['keyword'] = user_input
            while True:
                user_input = input("\nВведите минимальную зарплату: \nВаш выбор: ")
                if user_input.isdigit() == True:
                    user_vacancy_search.params['payment_from'] = int(user_input)
                    user_vacancy_search.get_vacancies()
                    user_vacancy_search.print_vacancies()
                    break
                else:
                    print("Неверный ввод")
            while True:
                user_input = input("\nЖелаете удалить какую-либо вакансию? (y/n)")
                if user_input == 'y':
                    user_input = input("Введите номер вакансии для удаления: ")
                    if user_input.isdigit() == True:
                        user_vacancy_search.delete_vacancy(int(user_input))
                        user_vacancy_search.print_vacancies()
                        continue
                    else:
                        print("Неверный ввод")
                else:
                    break
            user_input = input("\nЖелаете продолжить поиск вакансий? (y/n)")
            if user_input == 'y':
                continue
            else:
                flag = False



if __name__ == '__main__': user_interaction()
