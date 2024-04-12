#Escribir un programa que pida al usuario una palabra y muestre por pantalla el numero de veces que contiene cada vocal
import os 
os.system('cls' if os.name == 'nt' else 'clear')

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    tiempo = 0
    for letter in palabra:
        if letter == vocal:
            tiempo += 1
    print(" La vocal " + vocal + " aparece " + str(tiempo) + " veces ")