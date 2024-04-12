#Escriba un programa que almacene en una lista los numeros del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
import os 
os.system('cls' if os.name == 'nt' else 'clear')

numero = [1, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numero[-i], end=", ")