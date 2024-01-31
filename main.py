import baraja
import jugadas
# funcion pedir no implementada


    
#funcion comprobacion no implementada
        

#funcion pagar no implementada
def pagar():
  """
  Ganar con una mano mejor que la del crupier:

  Si el jugador tiene una mano con un valor más alto que la del crupier sin exceder 21, se le paga 1:1. Por ejemplo, si el jugador apuesta $10 y gana, recibe $10 adicionales, lo que hace un total de $20.
  Blackjack (21 con las dos primeras cartas):

  Si el jugador tiene un blackjack y el crupier no, generalmente se paga 3:2. Por ejemplo, si el jugador apuesta $10 y obtiene un blackjack, se le pagaría $15 adicionales, haciendo un total de $25.
  """
  pass
#funcion me_voy no implementada
def me_voy():
  """
  Termino de jugar
  """
  pass

#####################################################


inicial = baraja.mano_inicial()

suma_jugador = baraja.baraja[inicial[0][0]] + baraja.baraja[inicial[0][1]]
suma_crupier = baraja.baraja[inicial[1][0]] + baraja.baraja[inicial[1][1]]

#print(inicial)
print("-----------------------------------------------------------------")

print(f"Tu mano es: [{inicial[0][0]}] [{inicial[0][1]}] y suma", suma_jugador)
print(f"La mano del crupier es: [{inicial[1][0]}] [¿?] y por ahora suma", baraja.baraja[inicial[1][0]])
print("¿Que quieres hacer? \n[1] Pedir\n[2] Plantarse\n[3] Aumentar apuesta \n[4] Dividir juego")


#try:
jugador_decide = int(input("Por favor, selecciona SOLO EL NUMERO de la opcion elegida: "))
if jugador_decide == 1:
    print("Has elegido pedir otra carta.")
    baraja.pedir_jugador()
elif jugador_decide == 2:
    #llamar a funcion plantarse
    jugadas.plantar(inicial,suma_jugador,suma_crupier)
elif jugador_decide == 3:
    #Elige aumentar apuesta
    pass
else:
    #Elige dividir juego 
    pass
#except:
#    print("No has ingresado una opcion correcta")
    