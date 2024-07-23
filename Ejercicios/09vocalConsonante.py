letra = input("Ingresa una consonante: ").lower() #Forma 1 lower
#letra = letra.lower()# indicamos solo MINÚSCULAS con lower, Forma 2 lower
if letra == "a" or "e" or "i" or "o" or "u":
    print(f"Forma 1 La letra ingresada es una vocal {letra}")
if letra in "aeiou": # Forma 1 usando in en string
    print("La letra ingresada es una vocal")
if letra == "a" or letra =="e" or letra =="i" or letra =="o" or letra =="u":#Forma 2 comparando uno a uno
    
    print(f"Por favor indica un CONSONANTE pusistes la vocal {letra}")
else:
    print(f"Felicidades pusistes la consonante {letra}")