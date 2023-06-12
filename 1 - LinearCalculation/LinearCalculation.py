# Лінійний обчислювальний процес
# Студнента групи КМ-22-1
# Гаркуші Сергія
import math

def readFloat(name):
    print(f"Please enter {name}: ", end="")
    output = float(input())
    if output > 0:
        return output
    else:
        print(f"Incorrect input: {name} is negative. |{name}| will be used instead.")
        return math.fabs(output)

r1 = readFloat("R1")
r2 = readFloat("R2")

if r1 >= r2:
    roundSqr = math.pi * (r1 * r1 - r2 * r2);
    print(f"R1={r1},R2={r2},s={roundSqr}")
else:
    print("Incorrect input: R1 < R2.")
