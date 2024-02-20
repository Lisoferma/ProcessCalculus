__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для задания 6."""


def count_multiple_3_not_5(data: list):
    """Подсчитать количество чисел в списке кратных 3 и не кратных 5.

    data: список чисел.
    """
    result: int = 0

    for number in data:
        if number % 3 == 0 and number % 5 != 0:
            result += 1

    return result
