"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

n = input('Enter your number that > 0 ')
a = 0
for x in n:
    while int(x) > a:
        a = int(x)
print(a)