print("Ingresa las calificaciones del alumno: ")
practicas = float(input("Calificación de Prácticas"))
participacion = float(input("Calificación de Participación"))
examen = float(input("Calificación del Examen"))
practicas *= 0.40 # lineas 5,6,7 se pueden poner de las dos formas
participacion = participacion * 0.20
examen = examen * 0.40
final = practicas + participacion + examen
print(f"Esta es la calificación final del alumno : {final:.2f}")