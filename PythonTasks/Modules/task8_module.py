__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для задания 8."""

import numpy as np


def get_b_array(a: np.ndarray, b: np.ndarray):
    """Получить массив 'b', элементы которого равны сумме элементов матрицы 'a',
    расположенных в определённой области.

    :param a: массив на основе которого будет заполнен массив 'b'.
    :param b: массив с результатом.
    """
    rows = b.shape[0]
    cols = b.shape[1]

    for i in range(0, rows):
        for j in range(0, cols):
            b[i, j] = b[i - 1, j] + a[i:rows, j + 1].sum()           
