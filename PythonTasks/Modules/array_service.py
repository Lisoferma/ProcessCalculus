__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для работы с массиовм numpy."""

import numpy as np


def input_array(array: np.ndarray):
    """Ввод пользователем через консоль содержимого двумерного массива.

    :param array: float массив для ввода содержимого.
    """
    rows = array.shape[0]
    cols = array.shape[1]

    for i in range(0, rows):
        for j in range(0, cols):
            array[i, j] = float(input(f"[{i}, {j}]: "))
