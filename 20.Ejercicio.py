#Escribir un programa que pida al usuario 
import os 
os.system('cls' if os.name == 'nt' else 'clear')

n = int(input("Introduce un numero entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")