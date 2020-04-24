"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

sec_to_inp = int(input('Enter time in seconds '))
hours = sec_to_inp // 3600
while hours > 24:
    sec_to_inp = int(input('Are you insane?! Please enter smaller number '))
    hours = sec_to_inp // 3600
    if hours <= 24:
     break
residue = sec_to_inp % 3600
min = residue // 60
sec = residue % 60

print(f'The time is {hours}:{min}:{sec}')
