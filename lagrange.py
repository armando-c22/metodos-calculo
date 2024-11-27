def lag_inter(x, y, x_eval, orden):
    n = len(x)
    resultado = 0.0
    
    for i in range(orden + 1):
        term = y[i]
        for j in range(orden + 1):
            if j != i:
                term *= (x_eval - x[j]) / (x[i] - x[j])
        resultado += term
    
    return resultado

x_puntos = [-4, 3, 10]
y_puntos = [0.79053799, 481.38335029, 598744.17151978]

y_real = 199937.84687411427

x_eval = 15

resultado_1er_orden = lag_inter(x_puntos, y_puntos, x_eval, 1)
error_1er_orden = abs(y_real - resultado_1er_orden) / y_real
print(f"Interpolación de 1er orden en f(x) = {x_eval}: {resultado_1er_orden}")
print(f"Error absoluto de 1er orden en f(x) = {x_eval}: {error_1er_orden}%")
resultado_2do_orden = lag_inter(x_puntos, y_puntos, x_eval, 2)
error_2do_orden = abs(y_real - resultado_2do_orden) / y_real
print(f"Interpolación de 2do orden en f(x) = {x_eval}: {resultado_2do_orden}")
print(f"Error absoluto de 2do orden en f(x) = {x_eval}: {error_2do_orden}%")
