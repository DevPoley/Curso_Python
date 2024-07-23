total = 1000
print("Bienvenido a tu banco\n\
    1. Ingresar dinero:\n\
    2. Sacar dinero:\n\
    3. Salir:")
opcion = int(input())
if opcion == 1:
    ingreso = float(input("Cuanto dinero deseas ingresar: "))
    total += ingreso
    print(F"Has ingresado {ingreso} € y el total ahora en cuenta es {total} €") 
elif opcion == 2:
    retirada = float(input("Cuanto dinero deseas sacar: "))
    if total - retirada <0:
        print(f"Saldo insuficiente solo dispones de {total}")
    else:    
        total -= retirada
        print(F"Has sacado {retirada} € y el total ahora en cuenta es {total} €") 
elif opcion == 3:
    print("Gracias por usar el banco")
    quit() # No olvidar las llaves al final sino dará ERROR
else:
    print("Opcion no valida selcciona 1,2 o 3 para operar")