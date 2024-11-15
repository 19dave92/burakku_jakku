import os
from entities.Jugador import Jugador
from entities.Crupier import Crupier

def crear_jugadores():
    """_summary_

    Returns:
        dict: contiene los nombres de los jugadores (Key) y las instancias (Value)
    """

    diccionario_jugadores = {}  #_ Diccionario para almacenar el nombre y la instancia del jugador.
    nro_de_repetidos = 2

    while(True):
        try:
            os.system('cls')
            cantidad_jugadores = int(input("¿Cuantos jugadores seremos hoy?\n>>> "))
        except:

            print("Ingresa solo numeros enteros.")

        else: #Ejecuta el codigo si el try no tuvo ningun error.

            if (cantidad_jugadores > 0 and cantidad_jugadores <= 7):

                #Advertimos que si el usuario ingresa mas de 1 jugador su nombre se modificará
                if (cantidad_jugadores > 1):
                    print("\nSi tu nombre se repite, agregaremos un parentesis con un numero para diferenciarte.\n")
                
                for numero_de_jugador in range(1, cantidad_jugadores + 1):

                    nombre_jugador = input(f"\nIngrese el nombre del jugador {numero_de_jugador}: ").upper()
                    
                    ###################### CARGA DE JUGADORES ###############################################
                    ###################### EL DICCIONARIO ES LLENADO CON LAS INSTANCIAS DE LA CLASE JUGADOR.# 
                    ###################### CADA JUGADOR ES UN VALUE DEL DICT, LA KEY ES EL NOMBRE. ##########
                    if nombre_jugador in diccionario_jugadores: 
                        nombre_jugador = nombre_jugador + f" ({nro_de_repetidos})"
                        nro_de_repetidos = nro_de_repetidos + 1
                        
                    diccionario_jugadores[nombre_jugador] = Jugador(nombre_jugador)
                    ########################################################################################
                
                print("\nEs importante jugar con precaución, si tus fichas se agotan no puedes continuar.")
                
                # Creamos una instancia de crupier y lo agregamos como jugador al diccinaorio.
                diccionario_jugadores['crupier'] = Crupier()
                
                break
            else:
                print("Lo siento, los jugadores deben ser entre 1 y 7")

    return diccionario_jugadores


