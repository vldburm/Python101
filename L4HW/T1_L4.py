"""
Task 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
file_name, hours, rate, bonus = argv
calculation = (int(hours) * int(rate)) + int(bonus)
print(f"Your salary is equal to {calculation}")

#python T1_L4.py 2 100 100

