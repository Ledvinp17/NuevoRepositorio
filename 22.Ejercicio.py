#Escribir un programa en el que pregunte al usuario por una frase y una letra y muestre por pantalla el numero de veces que aparece la letra 
#en la frase
import os 
os.system('cls' if os.name == 'nt' else 'clear')

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))