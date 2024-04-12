#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palindromo
import os 
os.system('cls' if os.name == 'nt' else 'clear')

palabra = input("Introduce una palabra: ")
reversed_palabra = palabra
palabra = list(palabra)
reversed_palabra = list(reversed_palabra)
reversed_palabra.reverse()
if palabra == reversed_palabra:
    print("Es un palindromo")
else:
    print("No es palindromo")