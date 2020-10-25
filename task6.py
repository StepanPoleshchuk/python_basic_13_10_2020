'''
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено
'''


def my_count(start):
    while True:
        yield start
        start += 1


def my_cycle(args):
    while True:
        for i in args:
            yield i


def my_gen(start, stop):
    for i in my_count(start):
        if i > stop:
            break
        else:
            print(i)


def my_copy(user_list, n, lines='\n'):
    copy = 1
    for i in my_cycle(user_list):
        if copy > n:
            break
        copy += 1
        print(i, end=lines)  #не переходя на новую строку


while True:
    try:
        count_start = int(input('первое число: '))
        count_stop = int(input('последнее число: '))
        my_gen(count_start, count_stop)
        break
    except ValueError:
        print('должны быть целые числа')
        continue
while True:
    try:
        copy_data = input('введите элементы списка через пробел: ').split()
        copy_stop = int(input('количество повторений: '))
        if copy_stop < 1:
            print('количество повторений целое положительное')
            continue
        my_copy(copy_data, copy_stop)
        break
    except ValueError:
        print('количество повторений должно быть числом')
        continue

#my_copy("ха", 7, lines='')  #генерация смеха в строку
