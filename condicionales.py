# Hay que respetar los espacios sino da error expected expresion pylance
numero = float(input("Introduce un número positivo: "))
if numero < 0:
    print("El número introducido no es positivo")
elif     numero == 0:
    print("El número introducido es cero")
else:
    print("El número introducido es positivo")