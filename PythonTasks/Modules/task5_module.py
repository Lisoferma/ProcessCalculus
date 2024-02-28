__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для задания 5."""


def calculate_sum(data: list):
    """Вычислить сумму a[i] / i!, где i от 0 до n (n не включительно).

    :param data: список данных для нахождения суммы.
    """
    result = 0
    last_factorial = 1

    for i in range(1, len(data)):
        last_factorial *= i
        result += data[i] / last_factorial

    return result
