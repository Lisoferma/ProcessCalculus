__author__ = "Lisoferma"

# Задание №677в Дана действительная матрица [aij] i = 1, ..., n.
# Получить действительную матрицу [bij] i = 1, ..., n
# элемент bij которой равен сумме элементов данной матрицы расположенных в области,
# определяемой индексами i,j так, как показано на рисунке 36в (область заштрихована).
# https://ivtipm.github.io/Programming/Glava20/index20.htm#z677

import numpy as np
from Modules import array_service, task8_module

# Размеры массивов
rows: int
cols: int

# Массив вводимый пользователем
a: np.ndarray

# Массив с результатом
b: np.ndarray

rows = int(input("Введите количество строк массива: "))
cols = int(input("Введите количество столбцов массива: "))

a = np.zeros((cols, rows), float)
b = np.zeros((cols, rows), float)

array_service.input_array(a)
task8_module.get_b_array(a, b)

print("\nМассив A:")
print(a)

print("\nМассив B:")
print(b)
