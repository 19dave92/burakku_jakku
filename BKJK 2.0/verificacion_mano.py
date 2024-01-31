def contiene_as(hand):
    for x in range(len(hand)):
        if ('AS' in hand[x] ):
            return True
            #print(salida)

    
def contiene_figura(hand):
    for x in range(len(hand)):
        if ('K' in hand[x] or 
            'Q' in hand[x] or 
            'J' in hand[x] or 
            '10' in hand[x]):
            return True           
            
        
#hand = ['K♥','AS♥']
#hand2 = ['7♥','8♥']
#hand3 = ['10♥','8♥']

#print(contiene_figura(hand2))