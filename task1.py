'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
'''


def count(wtime, cashtime, special):
    return wtime * cashtime + special

while True:
    try:
        data_time = float(input('введите выработку в часах\n'))
        data_cashtime = float(input('введите ставку в час\n'))
        data_special = float(input('введите премию\n'))
        print (f'Заработная плата сотрудника {count(data_time, data_cashtime, data_special)}')
        break
    except ValueError:
        print('Вы ввели не числа, пробуем все заново')
