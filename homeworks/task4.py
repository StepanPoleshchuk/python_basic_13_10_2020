'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} GO')

    def stop(self):
        print(f'{self.name} STOP')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self, limit=60):
        if self.speed > limit:
            print(f'Превышение скорости! Разрешенная скорость {limit} - Ваша скорость {self.speed}')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(TownCar):
    def show_speed(self, limit=40):
        super().show_speed(limit)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(self, speed, color, name)
        self.is_police = is_police


truck1 = WorkCar(44, 'black', 'MAN')
truck2 = WorkCar(39, 'red', 'MAZ')
driver1 = TownCar(77, 'white', 'FORD')
driver2 = TownCar(58, 'yellow', 'NISSAN')
truck1.show_speed()  #нарушитель грузовик
truck2.show_speed()  #грузовик
driver1.show_speed()  #нарушитель легковая
driver2.show_speed()  #легковая
bobik = PoliceCar(100, 'white', 'Uaz')
print(bobik.is_police)  #is_police True при создании экземпляра класса PoliceCar
