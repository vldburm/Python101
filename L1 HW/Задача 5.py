"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

rev = int(input('Specify your Income '))
exp = int(input('Specify your Expenses '))
if rev > exp:
    prof = rev - exp
    rent = prof / rev
    print(f'Sweet! Your profit is {prof}')
    employees = int(input('Specify how many employees do you have '))
    print(f'{prof/employees} for one worker')
elif rev == exp:
    print('Good job, but could be better')
else:
    print('Good luck, have fun')
