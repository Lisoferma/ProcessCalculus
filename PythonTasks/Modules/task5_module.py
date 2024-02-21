__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для задания 5."""

import math


def calculate_sum(data: list):
    """Вычислить сумму a[i] / i!, где i от 0 до n (n не включительно).

    :param data: список данных для нахождения суммы.
    """
    result = 0

    # исп пред значение факториала
    for i in range(0, len(data)):
        result += data[i] / math.factorial(i)

    return result
