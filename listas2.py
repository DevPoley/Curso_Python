'''
- len #Tamaño.
- append #agrega al final.
- insert #inserta en algún punto de la lista un elemento.
- extend #Agrega una lista dentro de otra.
- suma #Suma de listas.
- in #Hay un valor en la lista.
- index #Retorna el valor que esté en un índice.
- count #Cuantas veces se repite un número
- pop #Elimina el último elemento o el indice que se le indique
- remove #Elimina un elemento dependiendo de su valor
- clear #Limpia toda la lista
- reverse #Invierte el orden de los elementos
- sort #Ordena los elementos
'''
lista = [1,2,3]
print(lista)
print("El Tamaño de la lista es: ",len(lista)) # len nos devuelve el tamaño de la lista
lista.append(4)
print("lista.append(4)", lista) # agrega un elemento mas al final de la lista Res= [1, 2, 3, 4]
lista.insert(0,0)
print("lista.insert(0.0)", lista) # agrega 0 a la posicion 0 de la lista Res= [0, 1, 2, 3, 4]
lista.extend([5,6,7])
print("lista.extend([5,6,7])=", lista)# extiende el tamaño de la lista Res= ([5,6,7])= [0, 1, 2, 3, 4, 5, 6, 7]
lista = lista+[8,9,10]
print("Agregamos a lista", lista) # otra forma de sumar listas o add datos Res= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Sacamos lista completa con * : ", *lista)
numero = 15 # verificamos si un nº esta o no en la lista y nos devuelve su posicion en la lista 
if numero in lista:
    print("El numero", numero, "esta en la lista")
else:
    print(f"El numero, {numero}, no esta en la lista")
    print(lista.index(5))

lista2 = [45, 56, 65 ,76] # Devuelve 3, la cuarta posicion pero la tercera de la lista 0,1,2,3
print(lista2.index(76))
    
# CONSTRUCTOR list , usamos un constructor par crear una lista
lista_de_iterable = list ("Hola queridos") # crea lista de string() los separa cada uno como elemento
print(lista_de_iterable) # ['H', 'o', 'l', 'a', ' ', 'q', 'u', 'e', 'r', 'i', 'd', 'o', 's']

print(lista.count(3)) # Cuenta el numero de veces que se repite algo eneste caso el nº3  Res= 1

lista.pop() # Elimina el ultimo elemento de la lista
print("lista.pop()", lista)
lista.pop(2) # Elimina la posicion indicada de la lista, borra el indice
print("lista.pop()", lista)

lista.remove(5) # Borra el valor de ese índice
print("lista.remove(5)", lista)

lista.reverse()
print("lista.reverse()", lista) # Invierte el orde de la lista 9,8,7,6,5,....

lista.sort()
print("lista.sort", lista) # Ordena la lista de menor a mayor 1,2,3,4,5....

lista.clear()
print("lista.clear", lista) # vacia la lista