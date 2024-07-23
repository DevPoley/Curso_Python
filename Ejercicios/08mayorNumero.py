print("Ingresa dos números: ")
num1 = int(input("Nº1: "))
num2 = int(input("Nº2: "))

if num1 == num2:
    print("Los números son iguales")
elif num1 > num2:
   # print("El número mayor es: ", num1)
    print(f"El nº1: {num1} es mayor que el nº2: {num2} ")
elif num1 < num2 and num2 == num1*2:
    print(f"El nº2 : {num2} es el doble que el nº1: {num1}")
else :
    print("El número mayor es: ", num2)