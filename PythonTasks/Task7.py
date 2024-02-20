__author__ = "Lisoferma"

# Задание №335в Дано натуральное число n. Вычислить сумму 1 / (k^2)!, где k от 1 до n.
# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178

from Modules import task7_module


# Количество итераций, задаваемое пользователем
n: int

# Результат суммы
result: float

print("Вычислить сумму 1 / (k^2)!, где k от 1 до n.")

n = int(input('Введите n: '))

result = task7_module.calculate_sum(n)
print(f"Результат: {result:.10f}")
