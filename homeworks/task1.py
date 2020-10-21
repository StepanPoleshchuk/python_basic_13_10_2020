"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
test_list = [2.5, 1, 'lesson', [1, 2, 3]]
test_list.append(True)
test_list.append({'name': 'Stepan', 'surname': 'Poleshchuk'})
print(type(test_list))
for itm in test_list:
    print(type(itm))
