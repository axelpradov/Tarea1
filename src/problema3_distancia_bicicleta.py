# Problema 3: Distancia que recorrerá una bicicleta

import math 

gravedad: float = 9.81  # m/s² — constante de aceleración gravitacional

def anguloEngranaje(n : float) -> float:
    return 2 * math.pi * n

def calcularDistancia(n : float, r1 : float, r2 : float, r3 : float) -> float:
    
    anguloPedal= anguloEngranaje(n)
    distancia: float = (anguloPedal * r1 * r3 )/ r2

    return distancia

def validarDatos(mensaje : str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Ingresa un valor mayor o igual a 0")
        except ValueError:
            print("Ingresa un número")

vueltas = validarDatos("Ingresa el número de vueltas: ")
radioEngranaje1 = validarDatos("Ingresa el valor del radio del engranaje de los pedales (r1) en metros: ")
radioEngranaje2 = validarDatos("Ingresa el valor del radio del engranaje de la llanta trasera (r2) en metros: ")
radioRueda = validarDatos("Ingresa el valor del radio de la rueda (r3) en metros: ")
distancia = calcularDistancia(vueltas,radioEngranaje1,radioEngranaje2,radioRueda)

print(f"distancia recorrida por la bicicleta: {distancia:.4f} m")