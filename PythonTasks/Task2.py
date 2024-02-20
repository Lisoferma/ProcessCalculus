__author__ = "Lisoferma"

# Задание №37 Даны действительные числа a, b, c.
# Удвоить эти числа, если a ≥ b ≥ c, и заменить их абсолютными значениями, если это не так.
# https://ivtipm.github.io/Programming/Glava02/index02.htm#z37


# Числа задаваемые пользователем
a: float
b: float
c: float

print("Удвоить числа a, b, c, если a ≥ b ≥ c, и заменить их абсолютными значениями, если это не так.")

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

if a >= b >= c:
    a *= 2
    b *= 2
    c *= 2
else:
    a = abs(a)
    b = abs(b)
    c = abs(c)

print(f"a = {a:.2f}\n"
      f"b = {b:.2f}\n"
      f"c = {c:.2f}")
