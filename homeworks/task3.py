'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {
        'wage': 0,
        'bonus': 0
    }

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name + " " + self.surname}')

    def get_total_income(self):
        amount = 0
        for value in self._income.values():
            amount += value
        print(f'Доход сотрудника {amount}')


Vlad = Position('Vladimir', 'Putin', 'GreatPerson', 1000000, 500000)
Dima = Position('Dmitri', 'Medvedev', 'GreatestPerson', 800000, 300000)
Vlad.get_full_name()
Vlad.get_total_income()
Dima.get_full_name()
Dima.get_total_income()
