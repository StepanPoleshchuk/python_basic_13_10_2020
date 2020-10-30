'''
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''


with open('data2.txt', 'r', encoding='UTF-8') as file:
    user_data = file.readlines()
result_data = [itm.split() for itm in user_data]  #разбили на список списков по пробелу
print(f'Количество строк: {len(user_data)}\nКоличество слов в кажждой строке:')
for itm in result_data:
    print(len(itm), end=' ')
