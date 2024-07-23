a = float(input("Ingresa el valor de a: ")) # Convertimos a int(número), Forma 1
b = input("Ingresa el valor de b: ")
# a =int(a)
b =int(b) # Convertimos a int(número) Forma 2
resultado = a/b+1
print("El resuldato es: ", resultado)
# De esta forma le indicamos cuantos decimales queremos f"string {variable:,.2f}", la coma marcamos , al 1,000
print(f"El resultado es: {resultado:,.2f}")# Formateamos no olvidar la f al principio