#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar 

import os 
os.system('cls' if os.name == 'nt' else 'clear')

#Preguntar al usuario por la renta
renta = float(input("¿Cual es tu renta anual? "))

#condicional para determinar el tipo impositivo dependiendo de la renta 
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

#mostrar por pantalla el producto de la renta por el tipo impositivo 
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')