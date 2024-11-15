def contiene_AS(hand):
    for x in range(len(hand)):
        if ('AS' in hand[x] ):
            return True

def contiene_FIGURA(hand):
    for x in range(len(hand)):
        if ('K' in hand[x] or 
            'Q' in hand[x] or 
            'J' in hand[x] or 
            '10' in hand[x]):
            return True           

def esta_en_primera_posicion(posicion_carta):
    return posicion_carta == 0            

def carta_visible_AS(hand):
    
    for x in range(len(hand)):
        if ('AS' in hand[x] ):
            if (esta_en_primera_posicion(x)):
                print("¿Pagar seguro?")
                #TODO: Verificar si la segunda carta es figura
                contiene_FIGURA()
            return True
    
def contiene_FIGURA_crupier(hand):
    for x in range(len(hand)):
        if ('K' in hand[x] or 
            'Q' in hand[x] or 
            'J' in hand[x] or 
            '10' in hand[x]):
            return True           


#hand = ['8♥', 'AS♥']
hand = ['AS♥', '8♥']
#hand2 = ['7♥','8♥']
#hand3 = ['10♥','8♥']

#print(hand[0]) # >>> AS♥

#print(contiene_AS_crupier(hand))
