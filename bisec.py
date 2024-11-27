import math

# Definir la función f(x)
def f(x):
    return x * math.exp(5 - x)

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        return None, "El método de la bisección no se puede aplicar."
    
    iteracion = 0
    print(f"Iteración {iteracion}: a = {a}, b = {b}, f(a) = {f(a)}, f(b) = {f(b)}")
    
    c = a
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        iteracion += 1
        print(f"Iteración {iteracion}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}")
        
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return c, None

a = -1
b = 2
tolerancia = 0.001

raiz, error = bisection(a, b, tolerancia)
if error:
    print(error)
else:
    print(f"\nLa raíz aproximada es: {raiz}")
