"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции
"""

value = int(input('введите целое положительное число\n'))
new_value = value
max_number = 0
while new_value > 0:
    if new_value % 10 > max_number:
        max_number = new_value % 10
    new_value = new_value//10
print(max)
