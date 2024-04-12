#Escriba un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no 
import os 
os.system('cls' if os.name == 'nt' else 'clear')

edad = int(input("¿Cual es tu edad? "))

if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
