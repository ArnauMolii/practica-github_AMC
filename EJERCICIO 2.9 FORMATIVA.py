

# Solicitar al usuario los segundos
segundos = float(input("Introduce la cantidad de segundos: "))

# Calcular minutos y horas
minutos = segundos / 60
horas = segundos / 3600

# Mostrar el resultado
print(f"{segundos} segundos equivalen a {minutos:.2f} minutos y {horas:.2f} horas.")