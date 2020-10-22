'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''
def people(name, surname, bdyear, bdcity, city, email, phone):
    print(name, surname, bdyear, bdcity, city, email, phone)
people(city = 'Tver', email = 'tver@gov.ru', bdyear = 1995, surname = 'Poleshchuk', name = 'Stepan', phone = 88005553535, bdcity = 'Bologoe')
