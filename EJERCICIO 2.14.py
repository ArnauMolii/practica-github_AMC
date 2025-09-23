

import math

# Solicitar al usuario el diámetro del círculo
diametro = float(input("Introduce el diámetro del círculo: "))

# Calcular el radio
radio = diametro / 2

# Calcular el perímetro y el área
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)

# Redondear los resultados a un decimal
perimetro = round(perimetro, 1)
area = round(area, 1)

# Mostrar los resultados
print(f"El perímetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")