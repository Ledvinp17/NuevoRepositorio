#Escribir un programa que pida al usuario dos numeros y devuelva su division. Si el usuario no introduce numeros debe devolver un aviso de 
#error y si el divisor es cero tambien

import os 
os.system('cls' if os.name == 'nt' else 'clear')

n1 = float(input("Introduce el dividendo: "))
n2 = float(input("Introduce el divisor: "))

if n2 == 0:
    print("¡ERROR! No se puede dividir por 0.")
else:
    print(n1/n2)