# Робота на GITHUB - https://github.com/serhii-harkusha-dnu/python-practice/tree/main
# Розгалужувальний обчислювальний процес
# Студнента групи КМ-22-1
# Гаркуші Сергія
import math

def readFloat(name):
    print(f"Please enter {name}: ", end="")
    return float(input())

x = readFloat("x")
y = readFloat("y")

less = (x + y) / 2
more = 2 * x * y
if x < y:
    x = less
    y = more
else:
    x = more
    y = less

print(f"Result: x = {x}; y = {y}.")