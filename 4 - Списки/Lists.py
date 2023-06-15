# Робота на GITHUB - https://github.com/serhii-harkusha-dnu/python-practice/tree/main
# Списки
# Студнента групи КМ-22-1
# Гаркуші Сергія

def readInt(name):
    print(f"Please enter {name}: ", end="")
    return int(input())

k = readInt("K")
if k <= 2:
    print("Incorrect input: K <= 2.")
    exit()

f1 = 1
f2 = 1
fibonacci = [f1, f2]
i = 3
while i <= k:
    fNext = f1 + f2
    fibonacci.append(fNext)
    f1 = f2
    f2 = fNext
    i += 1

print(f"Fibonacci sequence: {fibonacci}")