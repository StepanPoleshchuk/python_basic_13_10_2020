'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''
def my_func(arg_1, arg_2, arg_3):
    if arg_1 <= arg_2 and arg_1 <= arg_3:
        return arg_2+arg_3
    elif arg_2 <= arg_1 and arg_2 <= arg_3:
        return arg_1+arg_3
    elif arg_3 <= arg_1 and arg_3 <= arg_2:
        return arg_1 + arg_2
try:
    a, b, c = input('введите 3 значения через пробел ').split()
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print('необходиммы числа')
print(my_func(a, b, c))
