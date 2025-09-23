

# Solicitar al usuario el radio y la altura
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

# Calcular el área y el volumen
area = 2 * .pi * radio * (radio + altura)
volumen = .pi * radio**2 * altura

# Mostrar los resultados con 2 decimales
print(f"El área de un cilindro es: {area:.2f}")
print(f"El volumen de un cilindro es: {volumen:.2f}")