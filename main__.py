import os
import bienvenida
import colores as estilo_texto
import modulo_reglas
import baraja
from Jugador import Jugador
from Crupier import Crupier

def crear_jugadores(diccionario_jugadores):

    nro_de_repetidos = 2 #variable para diferenciar de nombres que se repitan

    while True:
        try:    
            global cantidad_jugadores                                                       #Se designa como global porque sino no anda (¿?).
            os.system('cls')                                                                #Limpiamos la consola.
            cantidad_jugadores = int(input("¿Cuantos jugadores seremos hoy? \n>>> "))       #Ingresamos cantidad de jugadores. 
        except:
            print("Ingresa solo números enteros.")                                          #Cualquier entrada no esperada atrapa la excepcion y comienza un nuevo bucle.
        else:        
            if (cantidad_jugadores <= 7 and cantidad_jugadores > 0):
                if (cantidad_jugadores > 1):
                    print("Si tu nombre se repite, agregaremos un parentesis con un numero para diferenciarte.\n")
                for numero_de_jugador in range(1, cantidad_jugadores + 1):
            
                    nombre_jugador = input(f"Ingrese el nombre del jugador {numero_de_jugador}: ")

                    ######################CARGA DE JUGADORES
                    ######################EL DICCIONARIO ES LLENADO CON LAS INSTANCIAS DE LA CLASE JUGADOR. CADA JUGADOR ES UN VALUE DEL DICT, LA KEY ES EL NOMBRE.
                    if nombre_jugador in diccionario_jugadores: 
                        nombre_jugador = nombre_jugador + f" ({nro_de_repetidos})"
                        nro_de_repetidos = nro_de_repetidos + 1
                        
                    diccionario_jugadores[nombre_jugador] = Jugador(nombre_jugador)
                    #######################
                print("Es importante jugar con precaución, si tus fichas se agotan no puedes continuar.")
                diccionario_jugadores['crupier'] = Crupier()                                #Agregamos al crupier como jugador final.
                break
            else:
                print("Lo siento, los jugadores deben ser entre 1 y 7.")
             
################################################################################################
##################################### INICIO PROGRAMA ##########################################
################################ DECLARACION DE VARIABLES ######################################

diccionario_jugadores = {}  #Almacena los jugadores y sus objetos. Se crea en el flujo princiapal para evitar crear una variable que almacene el retorno de la función. 
cantidad_jugadores = 0
indice = 0                  #Para buscar la mano dentro de la lista               

################################################################################################
############################## HILO PRINCIPAL DE EJECUCION #####################################

bienvenida.splash_de_inicio()

# Primera etapa:
# ------- Leer reglas - carga de jugadores - apuestas - primera mano (2 cartas) ------------------------------------
#   
while True:
    print("¿Que quieres hacer? ( REGLAS / JUGAR )\n")
    decision_del_jugador = (input(">>> ").lower()).strip()
    #decision_del_jugador = "jugar"

    if (decision_del_jugador == "reglas"):
        while True:
            try:
                print("\nReglas basicas         [1]\nReglamento completo    [2]\n")   
                decision_del_jugador = int(input(f"Ingrese el {estilo_texto.yellow('numero')} de la opcion deseada: "))
            except:
                print(estilo_texto.red(f"Selecciona un {estilo_texto.subr('numero')} entero."))
            else:
                if (decision_del_jugador == 1):
                    modulo_reglas.reglas_basicas()
                    decision_del_jugador = "jugar"
                    break
                elif (decision_del_jugador == 2):
                    modulo_reglas.reglamento_completo()
                    decision_del_jugador = "jugar"
                    break
                else:
                    print(estilo_texto.red("Opcion no valida.\n"))

    if (decision_del_jugador == "jugar"):
        #Creamos los jugadores
        crear_jugadores(diccionario_jugadores)
        
        #obtenemos la mano para todos los jugadores incluido el crupier
        mano_inicial = baraja.mano_inicial(cantidad_jugadores)
        
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
            indice += 1
            
            if indice == len(listado_de_jugadores): 
                indice = 0  #Si no reiniciamos el indice despues cuando lo volvamos a utilizar dara "Error out of limit"    

        break
    else:
        print("Ingresa una opcion valida.")
# Fin de la primera etapa ==========================================================================================
        
# Segunda etapa
# ------- Abrir juego? (solo si tiene cartas iguales) / Doblar apuesta / Pedir carta / Plantarse -------------------
for i in listado_de_jugadores:
    if i != 'crupier':
        nombre_buscar = i
        jugador_buscado = diccionario_jugadores.get(nombre_buscar)
        if ((jugador_buscado.monto_apostado * 2) > (jugador_buscado.fichas_jugador)):
            print(f"{jugador_buscado.nombre_jugador}, ¿Que quieres hacer?\n\n       [1] Pedir carta\n       [2] Plantarse")
        else:
            print(f"{jugador_buscado.nombre_jugador}, ¿Que quieres hacer?\n\n       [1] Pedir carta\n       [2] Plantarse\n       [3] Doblar apuesta")
        while True:
            try:
                print("\nElije una opcion (numero)")
                decision_del_jugador = int((input(">>> ")).strip())
                break
            except:
                print("Por favor, ingresa el numero de la opcion elegida.")
        if (decision_del_jugador == 1):
            print("Ha pedido una carta")
        elif (decision_del_jugador == 2):
            print("Ha elegido plantarse")
        elif (decision_del_jugador == 3):
            print("Ha elegido doblar apuesta")



# Fin de la segunda etapa ==========================================================================================

# ####################################################################################################################
# #########################_PRIMER TEST DE COMPARACION DE PUNTOS_#####################################################        
# for i in listado_de_jugadores:
#     if i != 'crupier':
#         nombre_buscar = i
#         jugador_buscado = diccionario_jugadores.get(nombre_buscar)
#         if (sum(jugador_buscado.suma_mano_inicial) > sum(diccionario_jugadores['crupier'].valor_cartas)):
#             print(f"Jugador {jugador_buscado.nombre_jugador} gana")
#             jugador_buscado.pagar_simple()
#         elif (sum(jugador_buscado.suma_mano_inicial) == sum(diccionario_jugadores['crupier'].valor_cartas)):
#             print(f"Jugador {jugador_buscado.nombre_jugador} empata")
#         else: 
#             print(f"Jugador {jugador_buscado.nombre_jugador} pierde")
#             jugador_buscado.jugador_pierde()
# #########################_FIN PRIMER TEST DE COMPARACION DE PUNTOS_#################################################
# #################################################################################################################### 
       
print("------------------------------------------------------------fin ejecucion")