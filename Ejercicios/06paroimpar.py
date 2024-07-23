numero1 = int(input("Introduce PRIMER nº PAR "))
numero2 = int(input("Introduce SEGUNDO nº PAR "))
numeroPar1 = numero1%2 # si el resto es CERO el numero es PAR, sino es impar
numeroPar2 = numero2%2 # si el resto es CERO el numero es PAR, sino es impar
if  numeroPar1 == 0 and numeroPar2 == 0: 
    print(f"Los dos números son PARES y son el {numero1} y el {numero2}")
elif    numeroPar1 != 0 or numeroPar2 != 0:
    print(f"Al menos uno de los números es IMPAR y son el {numero1} y el {numero2}")
    if numeroPar1 != 0:
        print(f"El número {numero1} es IMPAR")
    else:
        print(f"El número {numero2} es IMPAR")
else:
    print(f"Los dos números son IMPARES son el {numero1} y el {numero2}")