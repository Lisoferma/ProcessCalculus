__author__ = "Lisoferma"

# Сравнение времени перемножения двух матриц используя:
# списки python, numpy array, torch tensor

import timeit
import random
import numpy as np
import torch


def matrixmult(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise Exception("Cannot multiply the two matrices. Incorrect dimensions.")

    c = [[0 for row in range(cols_b)] for col in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c[i][j] += a[i][k] * b[k][j]
    return c


rows = 300
cols = 300

# python list
list_a = [[random.randint(0, 100) for i in range(rows)] for j in range(cols)]
list_b = [[random.randint(0, 100) for i in range(rows)] for j in range(cols)]

time_list = timeit.timeit("matrixmult(list_a, list_b)", globals=globals(), number=50)
print(f"Python list: {time_list}")

# numpy array
np_array_a = np.random.randint(0, 100, (rows, cols))
np_array_b = np.random.randint(0, 100, (rows, cols))

time_np = timeit.timeit("np.dot(np_array_a, np_array_b)", globals=globals(), number=50)
print(f"Numpy array: {time_np}")

# pytorch tensor
torch_a = torch.randint(100, (rows,cols))
torch_b = torch.randint(100, (rows,cols))

time_torch = timeit.timeit("torch.mm(torch_a, torch_b)", globals=globals(), number=50)
print(f"PyTorch tensor GPU: {time_torch}")

# Python list:        180.20034584299998
# Numpy array:        1.0468405609999536
# PyTorch tensor CPU: 2.966437330999952
# PyTorch tensor GPU: 0.4551719490000039
