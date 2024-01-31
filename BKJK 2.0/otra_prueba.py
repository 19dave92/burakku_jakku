def contiene_as(hand):
    for x in range(len(hand)):
        if ('AS' in hand[x] ):
            return True
        else:
            return False
    
def contiene_figura(hand):
    for x in range(len(hand)):
        if ('K' in hand[x] or 
            'Q' in hand[x] or 
            'J' in hand[x] or 
            '10' in hand[x]):
            return True           
        else:
            return False
        
hand = ['K♥','AS♥']
hand_2 = ['7♥','8♥']

print(contiene_as(hand))