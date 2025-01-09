
def es_numero_tesla(numero):
    # Reducir el número a un solo dígito
    while numero >= 10:
        suma = 0
        while numero > 0:
            suma += numero % 10  # Sumar el último dígito
            numero //= 10        # Quitar el último dígito
        numero = suma

    # Comprobar si el dígito final es 3, 6 o 9
    return numero in [3, 6, 9]

# Prueba del programa
numero = int(input("Ingresa un número: "))
if es_numero_tesla(numero):
    print("Es un número Tesla.")
else:
    print("No es un número Tesla.")
