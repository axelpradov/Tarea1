# Problema 1: Altura máxima de un tiro vertical
#
# Para calcular la altura máxima consideramos un objeto lanzado verticalmente
# hacia arriba desde el suelo con una velocidad inicial v₀.
#
# Sabemos que la gravedad tiene un valor de 9.81 m/s² y actúa desacelerando
# el objeto conforme sube, hasta que su velocidad llega a cero en la cima.
#
# Tomemos la ecuación de velocidad:
#   v = v₀ - g*t
# En la altura máxima la velocidad es 0, entonces:
#   0 = v₀ - g*t  →  t = v₀ / g
#
# Definamos la ecuación de posición:
#   y = v₀*t - ½*g*t²
# Sustituyendo el tiempo de la cima obtenemos la altura máxima.

gravedad: float = 9.81  # m/s² — constante de aceleración gravitacional

def calcularAlturaMaxima(v0: float) -> float:
    # Calculamos el tiempo que tarda el objeto en llegar a la cima
    # usando t = v₀ / g  (cuando la velocidad se hace cero)
    tiempoCima: float = v0 / gravedad

    # Sustituimos ese tiempo en la ecuación de posición para obtener
    # la altura máxima: y = v₀*t - ½*g*t²
    alturaMaxima: float = v0 * tiempoCima - (0.5 * gravedad) * (tiempoCima ** 2)

    return alturaMaxima

# Inicializamos la velocidad en 0 para que el while arranque la validación
velocidadInicial: float = 0.0

# Utilizamos el while para que el programa siga pidiendo un valor
# hasta que el usuario ingrese uno mayor a cero
while velocidadInicial <= 0:
    # Utilizamos el try para que el programa intente convertir la entrada
    # a float. Si el usuario escribe letras, el except atrapa el error
    # y evita que el programa truene, pidiendo el dato de nuevo
    try:
        velocidadInicial = float(input("Por favor, ingresa la velocidad inicial (m/s): "))
        if velocidadInicial <= 0:
            print("Ingrese un valor válido (debe ser mayor a 0)")
    except ValueError:
        print("Ingrese un número válido")

print(f"Altura máxima: {calcularAlturaMaxima(velocidadInicial):.4f} m")
