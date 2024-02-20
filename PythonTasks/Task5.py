__author__ = "Lisoferma"

# Задание №136и Даны натуральное число n, действительные числа a1,..., an.
# Вычислить: сумму a[i] / !i, где i от 0 до n.
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136

from Modules import list_service, task5_module


# Список чисел, задаваемых пользователем
list_a = list()

# Размер списка, задаваемый пользователем
n: int

# Результат суммы
result: float

print("Даны натуральное число n, действительные числа a1,..., an.\n"
      "Вычислить: сумму a[i] / i!, где i от 0 до n.")

n = int(input('Введите n: '))

print("Введите содержимое списка: ")
list_service.input_list(list_a, n)

result = task5_module.calculate_sum(list_a)

print(f"Результат: {result:.2f}")
