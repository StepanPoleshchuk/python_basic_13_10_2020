'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''


def numbers(ball1, ball2, ball3):  #на вход идет 3 строки с баллами, на выходе имеем сумму баллов разделенных любыми нечисловыми символами
    num = ball1 + ball2 + ball3
    total = 0
    current = ' '
    for digit in num:
        if digit.isdigit():
            current = str(current)
            current = current + digit
        else:
            if current != ' ':
                total = total + float(current)
            current = 0
    return total


with open('data6.txt', 'r', encoding='UTF-8') as file:
    user_data = file.readlines()
origin_data = [lesson.split() for lesson in user_data]

result = {}
for lesson in origin_data:
    result[lesson[0][:len(lesson[0])-1]] = numbers(lesson[1], lesson[2], lesson[3])
print(result)
