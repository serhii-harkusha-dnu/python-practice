# Робота на GITHUB - https://github.com/serhii-harkusha-dnu/python-practice/tree/main
# Циклічний обчислювальний процес
# Студнента групи КМ-22-1
# Гаркуші Сергія
import math

resultWithFor = 1
for b in range(1, 5 + 1):
    s = 0
    for c in range(2, 10 + 1):
        s = s + math.tan(b * c)
    resultWithFor = resultWithFor * s
print(f"Result calculated using \"for\":   {resultWithFor}")

resultWithWhile = 1
b = 1
while b <= 5:
    s = 0
    c = 2
    while c <=  10:
        s = s + math.tan(b * c)
        c = c + 1
    resultWithWhile = resultWithWhile * s
    b = b + 1
print(f"Result calculated using \"while\": {resultWithWhile}")