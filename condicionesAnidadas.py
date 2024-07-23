edad = int(input("Ingresa tu edad: "))
if edad > 0 and edad <=110:#condicion combinada, si se cumple entras al if sino vas al else  final
# if 0 > edad < 100     Esta sería otra forma    
    if edad >= 18:
        print("Eres MAYOR de edad")
    else:
        print("Eres MENOR de edad")
else:
    print("Edad incorrecta a de ser mayor de 0 y menor de 110")