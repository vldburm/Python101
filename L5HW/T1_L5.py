"""
Task 1
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_list = []
while True:
    line = input("Заполни меня данными (для завершения нажми Enter): ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("task1.txt", "w") as file_obj:
        file_obj.writelines(my_list)