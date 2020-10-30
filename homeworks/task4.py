'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''


count_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open('inp_data4.txt', 'r', encoding='UTF-8') as file:
    with open('result_data4.txt', 'w', encoding='UTF-8') as result_file:
        while True:
            user_data = file.readline()  #читаем строку
            if user_data == '':
                break
            user_data = user_data.split(' — ')  #разбиваем по символу
            result_file.write(count_dict[user_data[0]] + ' — ' + user_data[1])  #собираем обратно с новым русским значением по английскому ключу
