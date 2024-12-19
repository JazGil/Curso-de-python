
var = input("Ingresa un valor: ")

# Intentamos convertir la entrada a un número
try:
    # Convertir a flotante 
    num = float(var)
    
    # Verifica si es un entero
    if num.is_integer():
        print("Es un entero.")
    else:
        print("No es un entero.")
except ValueError:
    print("Es una cadena de letras.")







#f = 30.0
#print(f.is_integer())
#f = 10.6
#print(f.is_integer())