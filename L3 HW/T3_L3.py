"""
Task 3
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""

def my_func(x , y, z):
    if x >= z and y >= z:
        return x + y
    elif x > y and x < z:
        return x + z
    else:
        return y + z
print(f'Сумма 2-х наибольших аргументов: {my_func(int(input("x: ")), int(input("y: ")),int(input("z: ")))}')
