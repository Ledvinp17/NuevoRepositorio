#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a 1000 euros mensuales. Escribir un 
#programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

import os 
os.system('cls' if os.name == 'nt' else 'clear')

print("Impuesto")

edad = int(input("¿Cual es tu edad? "))
salario = float(input("¿Cuales son tus ingresos mensuales? "))

if edad > 16 and salario >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")