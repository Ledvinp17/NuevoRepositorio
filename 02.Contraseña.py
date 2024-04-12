#Escribir un proograma que almacene la cadena de caracteres "contraseña" en una variable, pregunte al usuario por la contraseña
#e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y minisculas

import os 
os.system('cls' if os.name == 'nt' else 'clear')

key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")