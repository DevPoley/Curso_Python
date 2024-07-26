alumnos = {
    1:["Eugenio","Chaparro"], 
    2:["Maria", "Martinez"], 
    3:["Pepe","Fariaz"]}
print(alumnos[1]) # Res= ['Eugenio', 'Chaparro']
print(alumnos[2]) # 
print(alumnos[3]) # 
# print(alumnos[4]) # No existe es compribacion si entra al else del if
 
if 1 in alumnos: # con in comprobamos si existe el id/alumno
    print("Si existe el alumno con id 1, y se llama: ", alumnos[1])
else:
    print("No hay alumno con el id 1")
if 2 in alumnos:
    print("Si existe el alumno con id 2, y se llama: ", alumnos[2])
else:
    print("No hay alumno con el id 2")
if 3 in alumnos:
    print("Si existe el alumno con id 3, y se llama: ", alumnos[3])
else:
    print("No hay alumno con el id 3")
if 4 in alumnos:
    print("Si existe el alumno con id 4, y se llama: ", alumnos[4])
else:
    print("No hay alumno con el id 4")
    
    # Obtenemos el valor del diccionario con   diccionario.get  "get"
    print(alumnos.get(1,"El alumno 1 no existe")) # Res= ['Eugenio', 'Chaparro']
    print(alumnos.get(2,"El alumno 2 no existe")) # ['Maria', 'Martinez']
    print(alumnos.get(3,"El alumno 3 no existe")) # ['Pepe', 'Fariaz']
    print(alumnos.get(4,"El alumno 4 no existe")) # El alumno 4 no existe
    
    # Obtenemos las llaves(keys del diccinario) 
    print(alumnos.keys()) # Res= dict_keys([1, 2, 3])
    
    # Obtenemos los valores(values) del diccionario
    print(alumnos.values()) # Res= dict_values([['Eugenio', 'Chaparro'],.....
    
    # Obtenemos el valor con get
    print(alumnos.__getitem__(2)) # Res= ['Maria', 'Martinez']
    
    # Obtenemos todos los valores e ids, mismo resultado que print(alumnos)
    print(alumnos.items()) # Res= dict_items([(1, ['Eugenio', 'Chaparro']), (2, ['Maria', 'Martinez']),..
    
    # "null" = "none" en python
    # Vaciamos el diccionario alumnos
    print("Nuestro diccionario ahora contiene= ",alumnos.clear())
    if not alumnos: # Si no hay alumnos...
        print("El diccionario esta vacio")
    else:
        print("El diccionario no esta vacio")