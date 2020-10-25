'''
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''


from functions import my_range


print([itm for itm in my_range(start=20, stop=241) if ((itm % 20 == 0) or (itm % 21 == 0))])
