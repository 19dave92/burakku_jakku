import baraja



def plantar(inicial,suma_jugador,suma_crupier):
    '''
    Finaliza la mano y da lugar al turno del crupier
    Si el turno es del crupier, finaliza la mano total y se ejecuta la funcion de comprobacion
    '''

    print("Has decidido plantarte. Se revelará la mano del crupier.") 
    print(f"La mano del crupier es: [{inicial[1][0]}] [{inicial[1][1]}] y suma", suma_crupier )
    
    #llamar a comparacion

    
def comprobacion_crupier(inicial, suma_jugador, suma_crupier):
    """
    verifica que jugador esta mas cerca del 21 o si hay empate

    """
    if suma_crupier >= 17:
        if (suma_crupier > suma_jugador):
            print("La casa gana")
            #restar dinero al jugador
        else:
            print("La casa pierde")
            #llamar a la funcion pagar apuesta
    else:
        baraja.pedir_crupier(suma_crupier)
