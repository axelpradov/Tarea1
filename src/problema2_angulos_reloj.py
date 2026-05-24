# Problema 2: Ángulos de las manecillas del reloj
#
# Para calcular los ángulos consideramos un reloj de 12 horas donde
# los ángulos se miden desde las 12:00 en sentido de las manecillas del reloj.
#
# Tomemos la manecilla de minutos:
#   Da una vuelta completa (360°) en 60 minutos.
#   Por lo tanto avanza 360/60 = 6° por cada minuto.
#
# Tomemos la manecilla horaria:
#   Da una vuelta completa (360°) en 12 horas = 720 minutos.
#   Por lo tanto avanza 360/12 = 30° por cada hora.
#   Pero también se mueve mientras avanzan los minutos:
#   avanza 30/60 = 0.5° por cada minuto adicional.
#   Esto explica por qué las 3:00 y las 3:30 tienen ángulos distintos.
#
# Definamos la diferencia entre ambas manecillas:
#   Si la diferencia supera 180° tomamos el complemento (360° - diferencia)
#   porque el ángulo mínimo entre dos manecillas nunca puede ser mayor a 180°.

def calcularAngulosReloj(horas: int, minutos: int) -> dict:
    # La manecilla de minutos avanza 6° por minuto
    angMinuto: float = minutos * 6

    # La horaria avanza 30° por hora + 0.5° por minuto
    # Usamos horas % 12 para que las 12 se traten como 0
    angHoraria: float = (horas % 12) * 30 + minutos * 0.5

    # Calculamos la diferencia absoluta entre ambos ángulos
    diferencia: float = abs(angHoraria - angMinuto)

    # Si la diferencia es mayor a 180° tomamos el ángulo menor del otro lado
    if diferencia > 180:
        diferencia = 360 - diferencia

    return {"horaria": angHoraria, "minuto": angMinuto, "diferencia": diferencia}

# Inicializamos con valores fuera de rango para que los while arranquen
horas: int = 0
minutos: int = -1

# Utilizamos el while para seguir pidiendo horas hasta obtener un valor entre 1 y 12
while horas < 1 or horas > 12:
    # Utilizamos el try para intentar convertir la entrada a entero.
    # Si el usuario escribe letras o decimales, el except evita que el programa truene
    try:
        horas = int(input("Ingresa las horas (1-12): "))
        if horas < 1 or horas > 12:
            print("Ingresa un valor válido (1 a 12)")
    except ValueError:
        print("Ingresa un número entero")

# Mismo mecanismo para los minutos, cuyo rango válido es 0 a 59
while minutos < 0 or minutos > 59:
    try:
        minutos = int(input("Ingresa los minutos (0-59): "))
        if minutos < 0 or minutos > 59:
            print("Ingresa un valor válido (0 a 59)")
    except ValueError:
        print("Ingresa un número entero")

resultado = calcularAngulosReloj(horas, minutos)
print(f"Manecilla horaria:  {resultado['horaria']}°")
print(f"Manecilla minutos:  {resultado['minuto']}°")
print(f"Ángulo entre ellas: {resultado['diferencia']}°")
