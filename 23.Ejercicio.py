#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminara
import os 
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
