print("Ingresa dos valores")
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
auxiliar = a # esta auxiliar separa las cifras 
a = b
b = auxiliar
print(f"Aquí tienes los valores de a: {a} y de b: {b}")
# Si ponemos solo  a=b y b=a el valor que tomará será solo uno por eso usamos una variable auxiliar