#Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual y el numero de años, y muestre por pantalla el 
#capital obtenido en la inversion cada año que dura la inversion

import os 
os.system('cls' if os.name == 'nt' else 'clear')

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interes porcentual anual?"))
años = int(input("¿Años?"))
for i in range (años):
    cantidad *= 1 + interes / 100
    print("Capital tres " + str(i+1) + "años " + str(round(cantidad, 2)))