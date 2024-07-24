lista = ["Hola",
         "humano",
         "como",
         "estas",
         1,
         2,
         3.25,
         14,
         [
             4,5,6 # SubLista detro de otra Lista
         ]
         
         ]
print(lista[3]) #contamos valores desde 0(Hola) = primer elemento de la lista,7
print(lista[-1]) #nos da el último elemento de la lista
print(lista[-2]) #nos da el penúltimo elemento de la lista
print(lista[0:3]) #nos saca un rango de 0 hasta 3 serían >  Hola', 'humano', 'como
print(lista[2:]) #nos saca un rango desde 2º elemento(posicion 3) hasta  última serían > como', 'estas', 1, 2, 3.25, 14