'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников
'''


with open('data3.txt', 'r', encoding='UTF-8') as file:
    user_data = file.readlines()
result_data = [itm.split() for itm in user_data]  #разбили на список списков по пробелу
allpayment = 0
print('сотрудники, чья заработная плата < 20000:')
for itm in result_data:
    itm[1] = float(itm[1])  #из строки в число
    allpayment += itm[1]  #сумма всех зп
    if itm[1] < 20000:
        print(itm[0])
print(f'средняя заработная плата всех сотрудников: {allpayment/len(result_data)}')
