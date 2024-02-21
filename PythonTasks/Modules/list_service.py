__author__ = "Lisoferma"

"""Модуль содержит вспомогательные функции для работы со списком."""


# list передаётся по ссылке, т.к. тип изменяемый
def input_list(list_to_input: list, size: int):
    """Ввод пользователем через консоль содержимого списка.

    :param list_to_input: список для ввода содержимого.
    :param size: количество элементов для ввода.
    """
    for i in range(0, size):
        input_item = float(input(f"[{i}]: "))
        list_to_input[i] = input_item
