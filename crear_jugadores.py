import os

#Funcion para crear jugadores
def crear_jugadores(diccionario_jugadores):
    """Crea una diccionario que contiene las instancias de cada jugador. [Key = nombre_jugador][value = instancia_clase_jugador]
    
    Args:
        diccionario_jugadores (dict): recibe un diccionario vacio.
    """


    nro_de_repetidos = 2                                                                    #variable para diferenciar de nombres que se repitan

    while True:
        try:    
            global cantidad_jugadores                                                       #Se designa como global porque sino no anda (¿?).
            os.system('cls')                                                                #Limpiamos la consola.
            cantidad_jugadores = int(input("¿Cuantos jugadores seremos hoy? \n>>> "))       #Ingresamos cantidad de jugadores. Se usa como variable de control del bucle de carga,
        except:
            print("Ingresa solo números enteros.")                                          #Cualquier entrada no esperada atrapa la excepcion y comienza un nuevo bucle.
        else:                                                                               #Si no se levanta una excepcion ejecuta este bloque del codigo
            if (cantidad_jugadores <= 7 and cantidad_jugadores > 0):                        #La cantidad de jugadores debe ser minimo 1 y maximo 7
                if (cantidad_jugadores > 1):                    
                    print("Si tu nombre se repite, agregaremos un parentesis con un numero para diferenciarte.\n")
                
                for numero_de_jugador in range(1, cantidad_jugadores + 1):                  #Se usa el (1, variable + 1) para que el usuario vea el primer jugador como 1 y no como 0
            
                    nombre_jugador = input(f"Ingrese el nombre del jugador {numero_de_jugador}: ")

                    ######################__CARGA DE JUGADORES
                    ######################__EL DICCIONARIO ES LLENADO CON LAS INSTANCIAS DE LA CLASE JUGADOR. CADA JUGADOR ES UN VALUE DEL DICT, LA KEY ES EL NOMBRE.
                    if nombre_jugador in diccionario_jugadores: 
                        nombre_jugador = nombre_jugador + f" ({nro_de_repetidos})"
                        nro_de_repetidos = nro_de_repetidos + 1
                        
                    diccionario_jugadores[nombre_jugador] = Jugador(nombre_jugador)
                    #######################
                print("Es importante jugar con precaución, si tus fichas se agotan no puedes continuar.")
                diccionario_jugadores['crupier'] = Crupier()                                #Agregamos al crupier como jugador final.
                break
            else:
                print("Lo siento, los jugadores deben ser entre 1 y 7.")                    #Si se ingresa un numero menor que 1, el bucle no se corta.
             