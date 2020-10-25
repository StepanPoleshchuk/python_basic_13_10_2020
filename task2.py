'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''


from functions import my_range


def shift(*args):
    return [(user_list[i+1], user_list[i]) for i in my_range(len(user_list)-1)]  #возвращает список кортежей, в котором первый элемент сдвинут


while True:
    try:
        user_list = input('Введите список чисел через пробел\n').split()
        user_list = [float(x) for x in user_list]
        result = [current for current, prev in shift(user_list) if current > prev]
        print(result)
        break
    except ValueError:
        print('вы ввели не числа')
