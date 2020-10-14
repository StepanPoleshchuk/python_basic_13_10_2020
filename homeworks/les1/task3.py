"""
 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
"""

input_n = input('Введите число n, а я найду сумму чисел n + nn + nnn\n')
n = int(input_n)
nn = int(input_n*2)
nnn = int(input_n*3)
print(n+nn+nnn)
