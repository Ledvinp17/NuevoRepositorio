#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matematicas, Fisica, Quimica, Historia y Lengua) en una lista y la 
#muestre por pantalla
import os 
os.system('cls' if os.name == 'nt' else 'clear')

materias = ["matematicas", "fisica", "quimica", "Historia", "Lengua"]
for materias in materias:
    print("Yo estudio " + materias)