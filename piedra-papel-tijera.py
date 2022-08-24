# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:39:54 2022

@author: Lean
"""

# Escriba un programa que permita al usuario jugar contra la computadora. 
# El programa debe ofrecer un menú para lanzar el juego. Una vez iniciado el juego, se pedirá 
# al usuario ingresar el nombre de una de las armas elegibles: piedra, papel o tijera. 
# Pero el usuario, tiene algunas libertades. Por ejemplo, para 'tijera', 
# podrá ingresar 't', 'ti', 'tij', 'ije', 'iJer', 'TiJe', etcétera. Es decir, letras consecutivas 
# de la palabra 'tijera' con 1 o más letras y, además, puede mezclar mayúsculas y minúsculas. 
# El programa debe identificar correctamente la intención del usuario, así por ejemplo, si el 
# usuario ingresa ‘p’ no se sabe si el usuario desea seleccionar ‘papel’ o ‘piedra’ y esto debe 
# informarse al usuario para que vuelva a elegir un arma.
# Luego, la computadora realizará una elección de arma al azar; considere utilizar 
# la función “random.choice”. Una vez que se conozca el resultado se debe informar la opción 
# elegida por el usuario, la opción elegida por la computadora y el resultado final.
# El programa debe permitir jugar varias partidas sin cerrarse, salvo que el usuario 
# desee cerrar el juego.

#%% Opciones
var = input("Ingrsee 1 para jugar y 0 para salir: ")

while var == '1':
    lista = ["piedra", "papel", "tijera"]

    arma = input("Ingrese el arma a utilizar: ")

    #paso la cadena a minusculas para poder comparar
    arma.lower()

    while arma == "p" or arma == "ra":  
        arma = input("Ingrese una opcion valida: ")
  
    if lista[0].find(arma) != -1:
        arma = lista[0]   

    elif lista[1].find(arma) != -1:
        arma = lista[1]

    else:
         arma = lista[2]
    print("El arma que elegiste es: ", arma)
#%% maquina    

    import random
    arma_maq = random.choice(["piedra", "papel", "tijera"])
    
    print("El arma elegida por la maquina es: ", arma_maq)

#%%  Enfrentamiento

    if arma_maq == "piedra" and arma == "tijera":
        print("gano la maquina")
    
    
    elif arma_maq == "piedra" and arma == "papel":  
        print ("Ganaste")
    
    elif arma_maq == "papel" and arma == "piedra":
        print("gano la maquina")

    elif arma_maq == "papel" and arma == "tijera":
        print("Ganaste")
    
    
    elif arma_maq == "tijera" and arma == "papel":  
        print ("gano la maquina")
    
    elif arma_maq == "tijera" and arma == "piedra":
        print("Ganaste")

    else:
        print("Empate")

    var = input("Si quiere seguir jugando ingrese (1): ")

print("Fin del juego")