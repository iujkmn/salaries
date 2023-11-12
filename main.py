import requests
from terminaltables import AsciiTable
from itertools import count
import os
from dotenv import load_dotenv


def get_table(title, programming_language_information):
    table_data = [[
        'Язык программирования', 'Вакансий найдено', 'Вакансий обработано',
        'Средняя зарплата'
    ]]
    for language, vacancy in programming_language_information.items():
        table_data.append([
            language, vacancy['vacancies_found'],
            vacancy['vacancies_processed'], vacancy["average_salary"]
        ])
    table = AsciiTable(table_data, title)
    return table.table


def predict_salary(salary_from=None, salary_to=None):
    if salary_from and salary_to:
        expect_salary = int((salary_from + salary_to) / 2)
    elif salary_to:
        expect_salary = int(salary_to * 1.2)
    elif salary_from:
        expect_salary = int(salary_from * 0.8)
    else:
        expect_salary = None
    return expect_salary


def get_headhunter_vacancies(language, page=0):
    Moscow = 1
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": language,
        "page": page,
        "area": Moscow,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def get_headhunter_vacancies():
    programming_language_information = {}
    for language in [
            "Python", "Java", "Javascript", "Ruby", "PHP", "C++", "TypeScript",
            "Swift"
    ]:
        vacancies_processed = 0
        all_salaries = []
        for page in count(0):
            vacancies_json = get_HeadHunter_vacancies(language, page=page)
            if page >= vacancies_json['pages'] - 1:
                break
            for vacancy in vacancies_json['items']:
                salary = vacancy.get('salary')
                if salary and salary['currency'] == "RUR":
                    predicted_salary = predict_salary(
                        vacancy['salary'].get('from'),
                        vacancy['salary'].get('to'))
                    if predicted_salary:
                        vacancies_processed += 1
                        all_salaries.append(predicted_salary)
        average_salary = None
        if all_salaries:
            average_salary = int(sum(all_salaries) / len(all_salaries))
        programming_language_information[language] = {
            "vacancies_found": vacancies_json['found'],
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary
        }
    return programming_language_information


def get_superjob_vacancies(token, language, page=0):
    headers = {'X-Api-App-Id': token}
    Moscow = 4
    params = {'town': Moscow, 'keyword': f'Программист {language}', 'page': page}
    response = requests.get('https://api.superjob.ru/2.0/vacancies/',
                            headers=headers,
                            params=params)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def get_superjob_vacancies():
    programming_language_information = {}
    for language in [
            "Python", "Java", "Javascript", "Ruby", "PHP", "C++", "TypeScript",
            "Swift"
    ]:
        vacancies_processed = 0
        all_salaries = []
        for page in count(0):
            vacancies_json = get_SuperJob_vacancies(language, page=page)
            if not vacancies_json['objects']:
                break
            for vacancy in vacancies_json['objects']:
                predicted_salary = predict_salary(vacancy["payment_from"],
                                                  vacancy["payment_to"])
                if predicted_salary:
                    vacancies_processed += 1
                    all_salaries.append(predicted_salary)
        average_salary = None
        if all_salaries:
            average_salary = int(sum(all_salaries) / len(all_salaries))
        programming_language_information[language] = {
            "vacancies_found": vacancies_json['total'],
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary
        }
    return programming_language_information


def main():
    token = os.environ['SUPERJOB_TOKEN']
    load_dotenv()
    title = 'SuperJob_Moscow'
    print(get_table(title, get_superjob_vacancies()))
    title = 'HeadHunter_Moscow'
    print(get_table(title, get_headhunter_vacancies()))


if __name__ == "__main__":
    main()
