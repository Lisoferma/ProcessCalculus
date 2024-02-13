__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для работы со списком."""


def input_list(list_to_input: list, size: int):
    """Ввод пользователем через консоль содержимого списка.

    list: список для ввода содержимого.
    size: количество элементов для ввода.
    """
    for i in range(0, size):
        input_item = float(input(f"[{i}]: "))
        list_to_input.append(input_item)
