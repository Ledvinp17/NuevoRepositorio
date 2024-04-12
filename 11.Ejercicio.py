#Escribir un programa que pida al usuario una palabra y la muestre 10 veces por pantalla
import os 
os.system('cls' if os.name == 'nt' else 'clear')

texto = input("Introduce una palabra: ")
for i in range(10):
    print (texto)