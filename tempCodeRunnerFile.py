david = Jugador('david')
hand = ['AS♥', '8♥']
david.mano(hand)
print(sum(david.suma_mano_inicial))
david.apuesta()
david.doblar_apuesta()
david.pagar_bj()