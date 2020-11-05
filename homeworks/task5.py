'''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой, {self.title} в деле')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом, {self.title} в деле')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка маркером, {self.title} в деле')


pen1 = Pen('любимая ручечка')
pencil1 = Pencil('любимый карандашик')
handle1 = Handle('волшебный маркер')
pen1.draw()
pencil1.draw()
handle1.draw()
