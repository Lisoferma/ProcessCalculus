__author__ = "Lisoferma"

# Задание №8 Определить периметр правильного n-угольника, описанного около окружности радиуса r.
# https://ivtipm.github.io/Programming/Glava01/index01.htm#z8

from math import *


def get_polygon_perimeter(corners: int, radius: float):
    """Возвращает периметр правильного n-угольника,
    описанного около окружности радиуса r.

    corners: количество углов n-угольника.
    radius: радиус окружности.
    """
    return 2 * radius * corners * tan(pi / corners)


# Количество углов n-угольника, задаваемое пользователем
input_corners: int

# Радиус окружности, задаваемый пользователем
input_radius: float

print("Получить периметр правильного n-угольника, описанного около окружности радиуса r.")

input_corners = int(input('Введите количество углов n-угольника: '))
input_radius = float(input('Введите радиус окружности: '))

print("Периметр равен: "
      f"{get_polygon_perimeter(input_corners, input_radius):.2f}")
