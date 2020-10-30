'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''


with open('task1.txt', 'w', encoding='UTF-8') as file:
    user_data = True
    while user_data:
        user_data = input('вводите данные:  ')
        file.write(user_data + '\n')
