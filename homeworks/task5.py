'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


with open('data5.txt', 'w') as file:
    for i in range(10, 20, 2):
        file.write(str(i) + ' ')
with open('data5.txt', 'r') as file:
    user_data = file.read()
s = []
total = 0
num = ''
for digit in user_data:
    if digit != ' ':
        num = num + digit
    else:
        total += int(num)
        num = ''
print(total)
