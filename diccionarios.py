diccionario =  {}
diccionario = {"python":1,"java":2, "JavaScript":3}
print(diccionario) 
print("len(diccionario): ",len(diccionario)) # nos dice tamaño del diccionario

print("diccionario['python']: ",diccionario['python']) # Nos dice el lugar del parametro (1)

# Insertar - Agregar elemento al diccionario
diccionario['c++'] = 4
print("Agregando elemento", diccionario) # Nos muestra el nuevo diccionario con el nuevo elemento
# Eliminar elemento del dicionario
diccionario['c++'] = 5 # Cambiamos du posición en el diccionario
print("Cambiando posición elemento", diccionario) # 

del(diccionario['c++'])
print("Borrando elemento c++ del diccionario: ", diccionario)

# Agregamos elementos de una lista y una tupla
diccionario['c/c++'] = [4,5] # Agregamos elemento de una lista
print("Agregamos 2 elmentos mas: ", diccionario)
diccionario['c#/delphi'] = (6,7) # Agregamos elementos de una tupla (inmutable)
print("Agregamos 2 elmentos mas: ", diccionario)

diccionario['otros'] = {100,101,102}
print("otros lenguages: ", diccionario)