tupla = (1,2,3,"texto","humano",2)
print(tupla)
print("tupla[1]= ",tupla[1]) # Es como una lista pero inmutable
print("tupla[0:3]= ",tupla[0:3]) # Muestra un rango, cuenta desde el 0 hasta 3 posiciones, Res= 1,2,3
print("3 in tupla= ",3 in tupla) # Devuelve un True puesto que el 3 si está en la tupla
print("tupla.index(2)", tupla.index(2))
print("tupla.count(1)", tupla.count(1))
print("len(tupla)= ", len(tupla))

# Podemos convertir tupla en list y viceversa
lista = list(tupla)
print(lista)
tupla2 = tuple(lista)
print(tupla2)
# Con esta conversion nos permite mofidicar cada una de ellas para hacer accesible y modificable sus datos