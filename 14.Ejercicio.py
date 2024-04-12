#Escribir un programa que pida al usuario un numero entero positivo y muestre en pantalla la cuenta atras desde ese numero hasta cero separados por comas
import os 
os.system('cls' if os.name == 'nt' else 'clear')

n = int(input("Introdoce un numero entero positivo: "))
for i in range (n, -1, -1):
    print(i, end=", ")