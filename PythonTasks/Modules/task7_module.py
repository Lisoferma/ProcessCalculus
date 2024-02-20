__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для задания 7."""

import math


def calculate_sum(n: int):
    """Вычислить сумму 1 / (i^2)!, где i от 1 до n (включительно).

    n: количество итераций.
    """
    result = 0

    for i in range(1, n + 1):
        result += 1 / math.factorial(i * i)

    return result
