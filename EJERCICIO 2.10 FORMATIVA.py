

# Solicitar los números al usuario
dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))

# Calcular el cociente y el resto
cociente = dividendo / divisor
resto = dividendo % divisor

# Determinar si el dividendo es par o impar
if dividendo % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"

# Mostrar los resultados
print(f"El cociente es: {cociente}")
print(f"El resto es: {resto}")
print(f"El dividendo es {paridad}")