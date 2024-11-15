def esta_en_primera_posicion(posicion_carta):
    return posicion_carta == 0  

def contiene_AS_crupier(hand):
    
    for x in range(len(hand)):
        if ('AS' in hand[x] and esta_en_primera_posicion(x)):
            print("¿Pagar seguro?")
            
            return True
        

hand = ['8♥', 'AS♥']
hand_ = ['AS♥', '8♥']

print(contiene_AS_crupier(hand))
print(contiene_AS_crupier(hand_))