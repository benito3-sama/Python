materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
#recorrer materias como materia
for materia in materias:
    calificacion = input("¿Que nota has sacado en " + materia + "?")
    notas.append(calificacion)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + notas[i])