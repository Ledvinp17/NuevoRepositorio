#Escribir un programa que pida al usuario un numero entero y muestre por pantalla un tringulo rectangulo.
import os 
os.system('cls' if os.name == 'nt' else 'clear')
n = int(input("Introduce la altura del triangulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")