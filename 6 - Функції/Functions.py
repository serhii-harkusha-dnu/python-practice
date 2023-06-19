import math

def f(u: float, t: float) -> float:
    if u > t or t == 4:
        return u * u + 6 * t
    else:
        return u * u + 2 * t + 5

a = 3.11
b = 0.02
x = 2.31
y = 4.2
z = f(math.sqrt(x), y) + f(a * a, b * b) + f(math.fabs(a * a - 1), b) + f(y * math.pow(a - b, 2), x * math.pow(a + b ,2))

print(f"z = {z}")
