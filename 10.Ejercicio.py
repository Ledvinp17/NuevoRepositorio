#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en funcion de su repuesta le muestre un menu con los 
#ingredientes disponibles para que elija. Solo se puede elegir un ingrediente ademas de la mozzarella y el tomate que estan en todas las pizzas.
#al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y  todos los ingredientes que lleva
import os 
os.system('cls' if os.name == 'nt' else 'clear')

print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el numero correspondiente al tipo de pizza que quieres:")

#Decision sobre el tipo de pizza 
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t1- Pimiento\n\2- tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")

else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamon\n\t3- Salmon\n")
    ingredientes = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamon")
    else:
        print("salmon")



