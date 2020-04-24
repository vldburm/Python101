"""
Task 2
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def my_func(name, surname, byear, city, email, telephone):
    return ' '.join([name, surname, byear, city, email, telephone])
print(my_func(surname='Burmistrov', name='Vladislav', byear='1993', city='Moscow', email='geekbrains@mail.ru',
              telephone= '8-999-999-99-99'))