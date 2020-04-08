"""
Task 2:
Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input().
"""
user_input = input('Введите элементы списка, разделяя их пробелом: ')
my_list = user_input.split()
my_len = len(my_list)
if my_len % 2 == 0:
    i = 0
    while i < my_len:
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < my_len -1:
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
print(my_list)
