__author__ = "Lisoferma"

# Задание №178б Даны натуральные числа n, a 1...an.
# Определить количество членов ak последовательности a1,...,an: кратных 3 и не кратных 5.
# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178

from Modules import list_service, task6_module


# Список чисел, задаваемых пользователем
list_a = list()

# Размер списка, задаваемый пользователем
n: int

# Количество членов удовлетворяющих условию
count: int

print("Определить количество членов последовательности кратных 3 и не кратных 5.")

n = int(input('Введите n: '))

print("Введите содержимое списка: ")
list_service.input_list(list_a, n)

count = task6_module.count_multiple_3_not_5(list_a)

print(f"Результат: {count}")
