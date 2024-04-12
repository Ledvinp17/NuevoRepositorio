#Escribir un programa que pregunte al usuario los numeros ganadores de la loteria primitiva, los almacene en una lista y los muestre por
#pantalla ordenados de menor a mayor
import os 
os.system('cls' if os.name == 'nt' else 'clear')

guardado = []
for i in range(6):
    guardado.append(int(input("Introduce un numero ganador: ")))
guardado.sort()
print("Los numeros ganadores son " + str(guardado))