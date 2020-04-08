"""
Task 3:
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_dict = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'autumn'}
n = int(input('Enter the month number '))
if n <= 12 and n >= 1:
    if n == 1 or n == 12 or n == 2:
        print(season_dict.get(1))
        print(season_list[0])
    elif n == 3 or n == 4 or n == 5:
        print(season_dict.get(2))
        print(season_list[1])
    elif n == 6 or n == 7 or n == 8:
        print(season_dict.get(3))
        print(season_list[2])
    elif n == 9 or n == 10 or n == 11:
        print(season_dict.get(4))
        print(season_list[3])
else:
    print('You have entered a non-existent month')

