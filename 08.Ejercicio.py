#Escribir un programa que lea la puntuacion del usuario e indique su nivel de rendimiento, asi como la cantidad de dinero que recibira el usuario
import os 
os.system('cls' if os.name == 'nt' else 'clear')

bono = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuacion: "))
#Clasificacion por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
#Mostrar nivel de rendimiento 
if nivel == "":
    print("Esta puntuacion no es valida")
else:
    print("Tu nivel de rendimiento es %s" % nivel) 
    print("Te corresponde cobrar %.2f€" % (puntos * bono))