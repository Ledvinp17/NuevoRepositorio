#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un
#nombre anterior a la M y los hombres con un hombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su 
#nombre y sexo, y muestre por pantalla el grupo que le corresponde


import os 
os.system('cls' if os.name == 'nt' else 'clear')

nombre = input("¿Como te llamas? ")
sexo = input("¿Cual es tu sexo (M o H)? ")

if sexo == "M":
    if nombre.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)