"""
Task 1:
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

task_int = 3
task_float = 3.3
task_list = ['qwe', '5']
task_tuple = ('ewq', '6')
task_str = 'Stay home'
task_dict = {'Best online edu platform': 'GeekBrains'}

overall_list = [task_int, task_float, task_list, task_tuple, task_str, task_dict]
for x in overall_list:
    print(f'{x} is {type(x)}')
