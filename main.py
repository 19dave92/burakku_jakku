#import bienvenida
from modules.crear_jugadores import crear_jugadores
import modules.baraja as baraja
import os


indice = 0
#

# Primera etapa:
# ------- Leer reglas - carga de jugadores - apuestas - primera mano (2 cartas) ------------------------------------
# 

while(True):
    print("Que quieres hacer? ( REGLAS / JUGAR )\n")
    decision_del_jugador = (input(">>> ").lower()).strip()

    if (decision_del_jugador == "reglas"):
        
        break
        

    if (decision_del_jugador == "jugar"):
        #_Creamos los jugadores.
        diccionario_jugadores = crear_jugadores()

        # Obtenemos la mano para todos los jugadores incluido el crupier
        mano_inicial = baraja.mano_inicial(len(diccionario_jugadores))

        #Convertimos las KEY del diccionario en una lista para poder consultar el diccionario a traves de sus respectivos KEY
        listado_de_jugadores = list(diccionario_jugadores)
        
        #Cada jugador hace su apuesta menos el crupier
        print("Cada jugador debe hacer su apuesta para comenzar.\n")
        for i in listado_de_jugadores:
            if i != 'crupier':
                nombre_buscar = i
                jugador_buscado = diccionario_jugadores.get(nombre_buscar)
                jugador_buscado.apuesta()
                #jugador_buscado.pide_carta()

        os.system('cls')    

        #Entregamos las cartas a los jugadores incluido el crupier
        for i in listado_de_jugadores:
            nombre_buscar = i
            jugador_buscado = diccionario_jugadores.get(nombre_buscar)
            jugador_buscado.mano(mano_inicial[indice])
            #el metodo mano muestra las cartas de cada jugador.
            indice += 1
            
        indice = 0
        break
    else:
        #Se muestra si el jugador no ingresa REGLAS o JUGAR 
        print("Ingresa una opcion valida")


# IMPORTANTE: Si la primera carta del croupier es un AS, puede MIRAR LA CARTA ESCONDIDA.