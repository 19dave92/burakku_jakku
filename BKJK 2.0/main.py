import bienvenida
import colores as cs
import modulo_reglas
import baraja
from Jugador import Jugador

def crear_jugadores(diccionario_jugadores):

    nro_de_repeticion = 2 #variable para diferenciar de nombres que se repitan

    while True:
        try:    
            global cantidad_jugadores
            cantidad_jugadores = int(input("¿Cuantos jugadores seremos hoy? \n>>> "))
        except:
            print("Ingresa solo números enteros.")
        else:        
            if (cantidad_jugadores <= 7 and cantidad_jugadores > 0):
                print("Si tu nombre se repite, agregaremos un parentesis con un numero para diferenciarte.\n")
                for numero_de_jugador in range(1, cantidad_jugadores + 1):
            
                    nombre_ingresado = input(f"Ingrese el nombre del jugador {numero_de_jugador}: ")

                    if nombre_ingresado in diccionario_jugadores: 
                        nombre_ingresado = nombre_ingresado + f" ({nro_de_repeticion})"
                        nro_de_repeticion = nro_de_repeticion + 1
                    diccionario_jugadores[nombre_ingresado] = Jugador(nombre=nombre_ingresado)

                print("Es importante jugar con precaución, si tus fichas se agotan no puedes continuar.")    
                break
            else:
                print("Lo siento, los jugadores deben ser entre 1 y 7.")
        
            
################################################################################################
##################################### INICIO PROGRAMA ##########################################
################################ DECLARACION DE VARIABLES ######################################

diccionario_jugadores = {}
cantidad_jugadores = 0
indice = 0 #para buscar la mano dentro de la lista               

################################################################################################
############################## HILO PRINCIPAL DE EJECUCION #####################################

bienvenida.splash_de_inicio()



while True:
    print("¿Que quieres hacer? ( REGLAS / JUGAR )\n")
    decision_del_jugador = (input(">>> ").lower()).strip()

    if (decision_del_jugador == "reglas"):
        while True:
            try:
                print("\nReglas basicas         [1]\nReglamento completo    [2]\n")   
                decision_del_jugador = int(input(f"Ingrese el {cs.yellow("numero")} de la opcion deseada: "))
            except:
                print(cs.red(f"Selecciona un {cs.subr("numero")} entero."))
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
                    print(cs.red("Opcion no valida.\n"))


    if (decision_del_jugador == "jugar"):
        #Creamos los jugadores
        crear_jugadores(diccionario_jugadores)
        
        #Guardamos las cartas que se reparten
        mano_inicial = baraja.mano_inicial(cantidad_jugadores)
        
        #Obtenemos la lista de los jugadores
        listado_de_jugadores = list(diccionario_jugadores)
        
        #Cada jugador hace su apuesta.
        print("Cada jugador debe hacer su apuesta.")
        for i in listado_de_jugadores:
            nombre_buscar = i
            jugador_buscado = diccionario_jugadores.get(nombre_buscar)
            jugador_buscado.apuesta()
            
        
        #iteramos la lista de jugadores para entregue cartas a los jugadores
        for i in listado_de_jugadores:
            nombre_buscar = i
            jugador_buscado = diccionario_jugadores.get(nombre_buscar)
            jugador_buscado.mano(mano_inicial[0][indice])
            indice += 1
            
            if indice == len(listado_de_jugadores): indice = 0
            
        

        
        #TODO: verificar si puede abrir juego
        break
    else:
        print("Ingresa una opcion valida.")
print("------------------------------------------------------------fin ejecucion")