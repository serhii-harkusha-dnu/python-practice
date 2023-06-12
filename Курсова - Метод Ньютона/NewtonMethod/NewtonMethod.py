# Робота на GITHUB - https://github.com/serhii-harkusha-dnu/python-practice/tree/main
# Програма до курсової роботи
# Студнента групи КМ-22-1
# Гаркуші Сергія

def readFloat(name: str) -> float:
    print(f"Please enter {name}: ", end="")
    return float(input())

def readInt(name: str) -> int:
    print(f"Please enter {name}: ", end="")
    return int(input())

def readXValues(n: int) -> list:
    x0 = readFloat("x0")
    xn = readFloat("xn")
    xValues = []
    i = 0;
    while i <= n:
        xi = x0 + i * (xn - x0) / n
        xValues.append(xi)
        i = i + 1
    return xValues

def readYValues(n: int) -> list:
    yValues = []
    i = 0
    while i <= n:
        yi = readFloat(f"y[{i}]")
        yValues.append(yi)
        i = i + 1
    return yValues

def calculateDelta(n: int, yValues: list) -> list:
    dy = yValues.copy()
    delta = [dy[n]]
    i = 0
    while i <= n - 1:
        j = 0
        while j < n - i:
            dy[j] = dy[j + 1] - dy[j]
            j = j + 1
        dy.pop(n - i)
        delta.append(dy[n - i - 1])
        i = i + 1
    return delta

def calculatePn(x: float, n: int, xValues: list, delta: list) -> float:
    h = xValues[1] - xValues[0]
    q = (x - xValues[n]) / h
    s = delta[0]
    factorial = 1
    d = 1
    i = 0
    while i < n:
        factorial = factorial * (i + 1)
        d = d * (q + i);
        s = s + (delta[i + 1] * d) / factorial;
        i = i + 1
    return s

def readXOrStop() -> float:
    print("Enter x (leave empty to exit): ", end="")
    text = input()
    if text != "":
        return float(text)

n = readInt("n")
xValues = readXValues(n)
yValues = readYValues(n)
delta = calculateDelta(n, yValues)

print("Finite differences:")
print(f"y[{n}] = {delta[0]}")
print(f"deltay[{n - 1}] = {delta[1]}")
i = 2
while i <= n:
    print(f"delta{i}y[{n - i}] = {delta[i]}");
    i = i + 1

print("Pn(x) is ready. Please proceed with data verification.")
x = readXOrStop();
while x is not None:
    pn = calculatePn(x, n, xValues, delta)
    print(f"Pn({x:.8f}) = {pn:.8f}")
    x = readXOrStop()

print("")
print("Press enter to exit...")
input()