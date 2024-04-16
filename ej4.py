def f(x):
    """Función de la cual queremos encontrar la raíz."""
    return x**2 - 2

def df(x):
    """Derivada de f(x)."""
    return 2 * x

def biseccion(f, a, b, tol):
    """Método de bisección para encontrar la raíz de f en el intervalo [a, b]."""
    if f(a) * f(b) >= 0:
        print("Bisección requiere signos opuestos en los extremos del intervalo.")
        return None, None
    it = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        it += 1
    return (a + b) / 2, it

def secante(f, x0, x1, tol):
    """Método de la secante para encontrar la raíz de f."""
    it = 0
    while abs(x1 - x0) > tol:
        if f(x1) - f(x0) == 0:
            print("División por cero en secante.")
            return None, None
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
        it += 1
    return x1, it

def newton_raphson(f, df, x0, tol):
    """Método de Newton-Raphson para encontrar la raíz de f."""
    it = 0
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
        it += 1
    return x1, it

# Parámetros iniciales y tolerancia
a, b = 1, 2  # Intervalo para bisección
x0, x1 = 1, 2  # Puntos iniciales para secante
x_initial = 1.5  # Punto inicial para Newton-Raphson
tolerancia = 1e-6  # Tolerancia para la convergencia

# Ejecución de los métodos
raiz_biseccion, it_biseccion = biseccion(f, a, b, tolerancia)
raiz_secante, it_secante = secante(f, x0, x1, tolerancia)
raiz_newton, it_newton = newton_raphson(f, df, x_initial, tolerancia)

# Resultados
print(f"Método de Bisección: Raíz = {raiz_biseccion}, Iteraciones = {it_biseccion}")
print(f"Método de la Secante: Raíz = {raiz_secante}, Iteraciones = {it_secante}")
print(f"Método de Newton-Raphson: Raíz = {raiz_newton}, Iteraciones = {it_newton}")
