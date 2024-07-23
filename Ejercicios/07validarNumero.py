x = float(input("Ingresa el valor de X: "))
y = float(input("Ingresa el valor de Y: "))

ecuacion = (y**2)-1 # f(x,y)=raix(x)/y(al cuadrado) - 1

if ( ecuacion != 0): # prevenimos un resultado de 0 que da error, validamos 
 # otra forma x**(0.5), esto es exponente de 2
    resultado = (x**(1/2) / (ecuacion)) #raiz cuadrada de x ,y elevado a 2 menos 1
    print(f"Este es el Resultado: {resultado}")
else:
    print(f"El valor de Y no puede ser {y}")