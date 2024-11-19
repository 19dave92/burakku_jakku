

#Verifica si la mano contiene un AS
def contiene_AS(hand):
    """
    Verifica si la mano contiene un AS en cualquier posición
    """          
    for x in range(len(hand)):      # Recorremos la lista de cartas
        if ('A' in hand[x] ):       # Si el caracter 'A' está en la cadena de texto de la posicion actual, regresa TRUE
            return True
    
    return False

def contiene_FIGURA(hand):
    for x in range(len(hand)):
        if ('K' in hand[x] or 
            'Q' in hand[x] or 
            'J' in hand[x] or 
            '10' in hand[x]):
            return True
    return False           

def esta_en_primera_posicion(posicion_carta):
    return posicion_carta == 0            

def carta_visible_AS(hand):
    for x in range(len(hand)):
        if ('A' in hand[x] ):
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


############# Zona de pruebitas
"""
#hand = ['8♥', 'A♥']
hand = ['A♥', '8♥']
#hand = ['7♥','8♥']
#hand3 = ['10♥','8♥']

print(hand) # >>> AS♥

print(contiene_AS(hand))
"""