'''1.- El diccionario tendrá una lista con 3 empleados con nombre y edad. 
2.- El mismo diccionario tendrá una lista de 3 de autos con marca, modelo y   también cada auto tendrá 2 submodelos
4.- Accederemos a la edad del empleado número 3.
5.- Accederemos al segundo submodelo del auto número 2.'''
#TODO ESTE TRBAJO ES COMO JSON
# CREAMOS EMPRESA con 3 empleados y 3 coches
empresa = {
    'empleados' :[
        {'nombre': 'Maria','edad':20}, # Diccionario
        {'nombre': 'Esteban','edad':30}, # Diccionario
        {'nombre': 'Pepito','edad':25} # Diccionario
        ], 

'coches' :[
        {'marca':'Ford', 'modelo':'Mustang','submodelos':['Race I','Racer II']},
        {'marca':'Renaul', 'modelo':'Twingo','submodelos':['Lance','Peta']}, 
        {'marca':'Fiat', 'modelo':'Tipo','submodelos':['Space I','Space II']}
        ]
}
# Accedemos a dos valores concretos
# Res= La edad de  Pepito  es  25  años 
print("La edad de ",empresa ['empleados'][2]['nombre'],"es", empresa ['empleados'][2]['edad']," años ")

# Res= Pepito  tiene un coche marca  Fiat  del modelo Tipo  y llamado  Space II
print(empresa['empleados'][2]['nombre'], " tiene un coche marca ", empresa['coches'][2]['marca']," del modelo",
      empresa['coches'][2]['modelo']," y llamado ",empresa['coches'][2]['submodelos'][1])

# Res= La edad de  Maria es 20  años
print("La edad de ",empresa ['empleados'][0]['nombre'],"es", empresa ['empleados'][0]['edad']," años ")

# Res= Maria  tiene un coche marca  Ford  del modelo Mustang  y llamado  Race I
print(empresa['empleados'][0]['nombre'], " tiene un coche marca ", empresa['coches'][0]['marca']," del modelo",
      empresa['coches'][0]['modelo']," y llamado ",empresa['coches'][0]['submodelos'][0])

# Sacando el submodelo del coche 2(posicion 1)
print(empresa['coches'][1]['submodelos'][1])

# Sacando edad de Esteban, Res= La edad de Esteban es de  30 años
print("La edad de Esteban es de ",empresa['empleados'][1]['edad'], "años")
