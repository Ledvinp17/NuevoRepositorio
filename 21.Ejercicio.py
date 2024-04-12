#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por 
#la ultima
import os 
os.system('cls' if os.name == 'nt' else 'clear')

palabra = input("Introduce una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])