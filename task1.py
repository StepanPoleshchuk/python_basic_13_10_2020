'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def division(arg_1, arg_2):
    try:
        result=arg_1/arg_2
        return (result)
    except ZeroDivisionError:
        return ('Делить на ноль нельзя')

try:
    a = float(input('введите делимое '))
    b = float(input('введите делитель '))
    print(division(a,b))
except ValueError:
    print('Необходимо ввести числа')
