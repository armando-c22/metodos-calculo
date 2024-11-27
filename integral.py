import numpy as np

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    
    # Imprimir los valores de x y f(x)
    for i in range(n + 1):
        print(f"x_{i} = {x[i]:.4f}, f_{i} = sqrt(x_{i}) = {y[i]:.4f}")
    
    return integral

# Definir la función
def f(x):
    return np.sqrt(x)

# Ingresar los valores de la integral y el número de subdivisiones
a = input("Ingresa el valor de a (límite inferior): ")
b = input("Ingresa el valor de b (límite superior): ")
n = int(input("Ingresa el número de subdivisiones n: "))

# Convertir 'pi' a su valor numérico si está en la entrada
a = eval(a)
b = eval(b)

# Calcular la integral
resultado = trapezoidal_rule(f, a, b, n)

# Imprimir el resultado
print(f"El valor aproximado de la integral es: {resultado:.4f}")