#Escribir un programa que determine si el numero es par o impar
import os 
os.system('cls' if os.name == 'nt' else 'clear')

n = int(input("Introduce un numero entero: "))
if n % 2 == 0:
    print("El numero " + str(n) + " es par")
else:
    print("El numero " + str(n) + " es impar")