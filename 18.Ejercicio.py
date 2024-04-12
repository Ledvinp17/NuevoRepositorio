#Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo.

import os 
os.system('cls' if os.name == 'nt' else 'clear')

n = int(input("Introduce la altura del triangulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
