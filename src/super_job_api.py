from src.abstract_class_api import AbstractClassAPI
import requests
import os
import json

class SuperjobAPI(AbstractClassAPI):

    API_URL = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        self.params = {
            'keyword': None,
            'payment_from': None,
            'no_agreement': 1
        }
        self.headers = {
            'X-Api-App-Id': os.getenv('SuperJob')
        }
    @property
    def keyword(self):
        return self.params['keyword']

    @property
    def payment_from(self):
        return self.params['payment_from']

    def get_vacancies(self):
        response = requests.get(self.API_URL, params=self.params, headers=self.headers)
        with open('vacancies_super_job.json', 'w', encoding='utf-8') as f:
            vacancies_list = []
            num = 1
            for i in response.json()['objects']:
                vacancy = {
                                        'Вакансия No': num,
                                        'Должность': i['profession'],
                                        'Зарплата от': i['payment_from'],
                                        'Зарплата до': i['payment_to'],
                                        'Ссылка': i['link'],
                                        'Обязанности': i['candidat']
                }
                vacancies_list.append(vacancy)
                num += 1

            json.dump(vacancies_list, f)


    def print_vacancies(self):
        with open('vacancies_super_job.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for vacancy in vacancies_list:
                print(f'Вакансия No {vacancy["Вакансия No"]}')
                print(f"Должность: {vacancy['Должность']}")
                print(f"Зарплата от {vacancy['Зарплата от']} до { vacancy['Зарплата до']}")
                print(f"Ссылка: {vacancy['Ссылка']}")
                print(f"Обязанности: \n{vacancy['Обязанности']}")
                print()

    def delete_vacancy(self, vacancy_number):
        with open('vacancies_super_job.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for i in vacancies_list:
                if i['Вакансия No'] == vacancy_number:
                    vacancies_list.remove(i)

        with open('vacancies_super_job.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies_list, f)

