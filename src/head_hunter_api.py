from src.abstract_class_api import AbstractClassAPI
import json
import requests


class HeadHunterAPI(AbstractClassAPI):
    '''
    Класс по поиску вакансий на сайте HH
    '''

    def __init__(self):
        self.params = {
            'text': None,
            "area": 1,  # (1 is Moscow)
            "per_page": None,
            'salary_from': None,
            'only_with_salary': True,
            # 'experience': None,
        }

    @property
    def text(self):
        return self.params['text']

    @property
    def salary_from(self):
        return self.params['salary_from']

    @property
    def per_page(self):
        return self.params['per_page']

    def get_vacancies(self):
        print(self.params)

        response = requests.get('https://api.hh.ru/vacancies', params=self.params)
        if response.status_code == 200:
            print('Запрос получен успешно')
        else:
            print(f"Request failed with status code: {response.status_code}")

        with open('vacancies_HHru.json', 'w', encoding='utf-8') as f:
            vacancies_list = []
            num = 1
            for i in response.json()['items']:
                middle = 0
                if i['salary']['from'] and i['salary']['to']:
                    middle = i['salary']['from']
                elif i['salary']['from'] and not i['salary']['to']:
                    middle = i['salary']['from']
                elif i['salary']['to'] and not i['salary']['from']:
                    middle = i['salary']['to']
                vacancy = {
                    'Вакансия No': num,
                    'Зарплата': middle,
                    'Должность': i['name'],
                    'Требования': i['snippet']['requirement'],
                    'Обязанности': i['snippet']['responsibility']
                }
                vacancies_list.append(vacancy)
                num += 1
            json.dump(vacancies_list, f)



    def print_vacancies(self):
        with open('vacancies_HHru.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for vacancy in vacancies_list:
                print(f'Вакансия No {vacancy["Вакансия No"]}')
                print(f"Должность: {vacancy['Должность']}")
                print(f"Зарплата {vacancy['Зарплата']}")
                print(f"Требования: {vacancy['Требования']}")
                print(f"Обязанности: \n{vacancy['Обязанности']}")
                print()

    def delete_vacancy(self, vacancy_number):
        with open('vacancies_HHru.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for i in vacancies_list:
                if i['Вакансия No'] == vacancy_number:
                    vacancies_list.remove(i)

        with open('vacancies_HHru.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies_list, f)



