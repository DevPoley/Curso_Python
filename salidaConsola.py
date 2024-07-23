nombre = "Francisco" # variable 0
edad = 50 # variable 1
# FORMA UNA VARIABLES DIRECTAS
print("Hola humano tu nombre es  ", nombre, " y tu edad es ", edad)

# FORMA 2 VARIABLES PASADAS POR .format(variable,variable)
print("Hola humano tu nombre es {0} y tu edad es {1} adios {0}" .format(nombre, edad))

#le damos un formato propio 1= variable(0) 2= nº espacios(2) 3= nº decimales(3f)
# Hola humano tu nombre es Francisco y tu edad es 50.000 adios Francisco 
print("Hola humano tu nombre es {0} y tu edad es {1:2.3f} adios {0}" .format(nombre, edad))

#le damos un formato propio 1= variable(0) 2= nº espacios(10) 3= nº decimales(3f)
print("Hola humano tu nombre es {0} y tu edad es {1:10.3f} adios {0}" .format(nombre, edad))
# Hola humano tu nombre es Francisco y tu edad es     50.000 adios Francisco

# Aquí llamamos a la variable directamente y no a su posición
print(f"Hola humano tu nombre es {nombre} y tu edad es {edad} adios {nombre}")
# Tambien le podemos dar formato propio
print(f"Hola humano tu nombre es {nombre} y tu edad es {edad:10.3f} adios {nombre}")
