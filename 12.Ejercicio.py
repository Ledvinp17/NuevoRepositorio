#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)
import os 
os.system('cls' if os.name == 'nt' else 'clear')

edad = int(input("¿Cuantos años tienes? "))
for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")