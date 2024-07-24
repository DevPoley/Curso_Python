# NO PERMITE ELEMENTOS REPETIDOS

conjuntos = set() # Los conjuntos siempre se inicializan o declaran
conjuntos = {1,2,3,"Hola","humano"} # NO PERMITE DUPLICIDAD DE DATOS > 
print("Contenido de conjuntos es: ",conjuntos)# Res= {1, 2, 3, 'humano', 'Hola'}

conjuntos.add(4)
print(conjuntos) # Res= {1, 2, 3, 'Hola', 4, 'humano'} > NO ORDENADO

print("3 in conjuntos ",3 in conjuntos) # Res= True
conjuntos.discard(1)
print("conjuntos.discard(1) ", conjuntos) # Res= {2, 3, 4, 'Hola', 'humano'}