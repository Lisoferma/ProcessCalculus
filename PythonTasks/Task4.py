__author__ = "Lisoferma"

# Задание №115a Дано натуральное число n. Вычислить: сумму 1 / k, где k от 1 до n.
# https://ivtipm.github.io/Programming/Glava04/index04.htm#z115


print("Дано натуральное число n. Вычислить: сумму 1 / k, где k от 1 до n.")

n = int(input('Введите n: '))
result = 0

for i in range(1, n + 1):
    result += 1 / i

print(f"Результат: {result:.2f}")
