__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для задания 7."""

import math


def calculate_sum(n: int):
    """Вычислить сумму 1 / (i^2)!, где i от 1 до n (включительно).

    :param n: количество итераций.
    """
    if n == 0: return 0

    result = 1
    last_factorial = 1
    last_sqr = 1

    for i in range(2, n + 1):
        current_sqr = i * i

        for i in range(last_sqr + 1, current_sqr + 1):
            last_factorial *= i

        last_sqr = current_sqr
        result += 1 / last_factorial

    return result
