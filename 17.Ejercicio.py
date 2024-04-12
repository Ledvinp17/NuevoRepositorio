#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
import os 
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")