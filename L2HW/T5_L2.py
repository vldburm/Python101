"""
Task 5:
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них.
"""

n = int(input("Enter any number: "))
my_list = [9, 5, 3, 2, 1]
c = my_list.count(n)
for element in my_list:
    if c > 0:
        i = my_list.index(n)
        my_list.insert(i+c, n)
        break
    else:
        if n > element:
            j = my_list.index(element)
            my_list.insert(j, n)
            break
        elif n < my_list[len(my_list) - 1]:
            my_list.append(n)
print(my_list)