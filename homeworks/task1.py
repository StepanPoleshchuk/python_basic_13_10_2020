'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матрицы 3х2

31 22
37 43
51 86

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''


class Matrix:
    def __init__(self, original_matrix):
        self.original_matrix = original_matrix
        #print(self.original_matrix)

    def __str__(self):
        out = ''
        for i in self.original_matrix:
            for j in i:
                out = out + ' ' + str(j)
            out = out + '\n'
        return out

    def __add__(self, other):
        if len(self.original_matrix) == len(other.original_matrix) and len(self.original_matrix[0]) == len(other.original_matrix[0]):
            result = []
            for string in range(len(self.original_matrix)):  #индекс каждой строчки(горизонтали)
                new_string = []
                for value in range(len(self.original_matrix[string])):  #индекс каждого элемента в каждой строчке
                    new_string.append((self.original_matrix[string][value])+(other.original_matrix[string][value]))
                result.append(new_string)
            self.original_matrix = result
            return Matrix(self.original_matrix)
        else:
            raise TypeError('складываем только матрицы одного размера')


a = Matrix([[31, 22], [37, 43], [51, 86]])
b = Matrix([[1, 2], [3, 4], [5, 6]])
print(a)
print(b)
c = a + b
print(c)
