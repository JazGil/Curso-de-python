
def es_numero_tesla(numero):
    
    while numero >= 10: #Ensures that a number is processed if it is more than digit long.
        suma = 0 #Initializes the variable where the sum is accumulated.
        while numero > 0: #Processes the number digit by digit.
            suma += numero % 10  # Sum the last digit.
            numero //= 10        #Remove the last digit.
        numero = suma

    # Check if the last digit is 3, 6 o 9
    return numero in [3, 6, 9]


numero = int(input("Ingresa un número: ")) #Asks the user for a number.
if es_numero_tesla(numero):
    print("Es un número Tesla.")
else:
    print("No es un número Tesla.")
