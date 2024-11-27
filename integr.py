import numpy as np

def f(x):
    return x * np.exp(5 - x)

a = -1  # Límite inferior
b = 2   # Límite superior
m = 12  # Número de subintervalos

# Longitud de cada subintervalo
h = (b - a) / m

# Puntos de evaluación
x = np.linspace(a, b, m + 1)
fx = f(x)

# Pesos de Newton-Cotes para m = 12
if m == 12:
    w = np.array([1, 3, 3, 2, 4, 2, 4, 2, 4, 2, 3, 3, 1])

# Cálculo de la integral usando la regla de Newton-Cotes (Simpson compuesto en este caso)
integral = (h / 3) * np.dot(w, fx)

print(integral)








