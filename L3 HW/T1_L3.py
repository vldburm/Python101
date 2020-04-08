"""
Task 1
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_func(*args):
    try:
        argum1 = int(input('Добавьте делимое '))
        argum2 = int(input('Добавьте делитель '))
        result = argum1 / argum2
    except ZeroDivisionError:
        return 'Вы не можете делить на ноль'
    except ValueError:
        return 'Ошибка в значении'

    return result

print(f'Результат: {my_func()}')


