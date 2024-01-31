lista2 = ['8♦', '7♦']

def contiene_as(self):
    for x in range(len(self.hand)):
        if ('AS' in self.hand[x] ):
            return True
            #print("Esta en la posicion", lista2.index(lista2[x]))

def contiene_figura(self):
    for x in range(len(self.hand)):
        if ('K' in self.hand[x] or 'Q' in self.hand[x] or 'J' in self.hand[x] or '10' in self.hand[x]):
            return True           
        else:
            return False
        

#    for carta in self.hand:
#       suma_cartas_jugador = mazo.baraja[carta]