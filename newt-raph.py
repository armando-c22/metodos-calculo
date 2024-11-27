import math
import pandas as pd

tolerance = 0.001

def f(x):
    return math.exp(-x) - x

def df(x):
    return -math.exp(-x) - 1

x0 = 0

results = []

cnt = 0

while True:
    cnt += 1
    fx = f(x0)
    dfx = df(x0)
    x1 = x0 - fx / dfx
    results.append([cnt, x0, fx, dfx, x1])
    if abs(x1 - x0) < tolerance:
        break
    x0 = x1

df = pd.DataFrame(results, columns=["Iteracion", "x", "f(x)", "f'(x)", "x_nuevo"])


print("\nSe encontró la raíz f(x) = 0 con x =", x0, "con una tolerancia de", tolerance)
print("\nTabla de resultados:\n")

print(df)


