'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
'''


from functions import my_range


def printing():
    print(f'{user_data}! = ', end='')
    for i in my_range(start=1, stop=user_data):
        print(f'{i} * ', end='')
    print(f'{user_data} =', result[user_data], end='')


def fact(n):
    count = 0
    res = 1
    while count <= n:
        count += 1
        yield res
        res *= count


while True:
    try:
        user_data = int(input('Введите число, факториал которого хотим взять\n'))
        if user_data < 0:  #проверка на ввод отрицательного значения
            print('должно быть целое положительное число')
            continue
        result = [i for i in fact(user_data)]
        printing()
        break
    except ValueError:  #проверка на ввод символа
        print('должно быть число')
