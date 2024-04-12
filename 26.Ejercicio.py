#Escribir un programa que almacene las asignaturas de un curso (por ejemplo matematicas, fisica, quimica, historia, lengua) en una lista y la 
#muestre por pantalla
import os 
os.system('cls' if os.name == 'nt' else 'clear')

materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
n = []
for materia in materias:
    nota = input("¿que nota has sacado  en " + materia + "?")
    n.append(nota)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + n[i])