'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property
'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    _consumptions = []

    @abstractmethod
    def information(self):
        return

    @classmethod
    def consumption(cls):
        s = 0
        for i in cls._consumptions:
            s += i
        return f'количество ткани на все изделия {s}'


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.mass = self.size / 6.5 + 0.5
        super()._consumptions.append(self.mass)

    def information(self):
        print(f'размер {self.size}, количество ткани {self.mass}')


class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth
        self.mass = 2 * self.growth + 0.3
        super()._consumptions.append(self.mass)

    def information(self):
        print(f'рост {self.growth}, количество ткани {self.mass}')


bershka = Coat(50)
zara = Coat(44)
th = Suit(180)
lacoste = Suit(175)

bershka.information()
#print(Clothes._consumptions)
print(Clothes.consumption())
