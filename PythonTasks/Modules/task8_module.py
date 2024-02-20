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
            b[i, j] = get_sum_from_area(a, i, j)


def get_sum_from_area(array: np.ndarray, min_i: int, max_j: int):
    """Получить сумму содержимого массива на заданной области.
    :param array: массив содержащий данные для суммы.
    :param min_i: минимальный i индекс области.
    :param max_j: максимальный j индекс области.
    """
    result: float = 0.0
    rows = array.shape[1]

    for i in range(min_i, rows):
        for j in range(0, max_j + 1):
            result += array[i, j]

    return result
