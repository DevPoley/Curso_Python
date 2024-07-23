nombre = input("Ingresa tu Nombre: ")
edad = input("Ingresa tu Edad: ")
edad = int(edad) # parseamos el string de edad y lo convertimos a int sino lo usa como texto
print(f"Tu nombre es:  {nombre} y tu edad es de {edad} años")
dias =  edad * 365
print(f"Has vivido {dias:,} dias") # Agregando :, le decimos que separe las unidades 18,250 dias
print(dias/365)