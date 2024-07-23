print("Ingresa dos números ")
num1 = int(input("Nº1 "))
num2 = int(input("Nº2 "))
opcion = input("Selecciona la operación deseada\n\
S s= Suma\n\
R r= Resta\n\
D d=División\n\
M m=Multiplicación\n\
")
opcion = opcion.lower()

if opcion == "s":
    resultado = num1 + num2
elif opcion == "r":
    resultado = num1 - num2
elif opcion == "d":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("No se puede dividir por 0")
        quit()
elif opcion == "m":
    resultado =num1 * num2
else:
    print("No seleccionastes ninguna opción de s,r,d,m")
    quit()
print(f"El resultado de tu operación es : {resultado}")