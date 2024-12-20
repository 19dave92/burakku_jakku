import modules.baraja as mazo
import modules.verificacion_mano as vm

class Crupier:

    def __init__(self, hand=[]):
        
        self.mano_inicial_crupier = hand
        self.valor_cartas = 0
        
    def mano(self, hand):

        self.mano_inicial_crupier = hand
        #Para sumar el valor de cuando pide una carta
        #suma_cartas_jugador += mazo.baraja[self.hand[-1]]

        #sumar el total de la mano
        self.valor_cartas = [mazo.baraja[self.mano_inicial_crupier[0]],
                             mazo.baraja[self.mano_inicial_crupier[1]]]            
        
        #if (sum(valor_cartas) > 21 and vm.contiene_as(self.mano_inicial_crupier)):
        #    suma_cartas_jugador -= 10


# IMPORTANTE: Si la primera carta del croupier es un AS, puede MIRAR LA CARTA ESCONDIDA para ver si tiene BJ.
# Hay que revisar si la carta visible es un AS

        if (vm.contiene_AS(self.mano_inicial_crupier)       == True and 
            vm.contiene_FIGURA(self.mano_inicial_crupier)   == True      ):
            print(f"Cartas del CRUPIER: [{self.mano_inicial_crupier[0]}][{self.mano_inicial_crupier[1]}] - BURAKKU JAKKU")
        else:
            print(f"Cartas del CRUPIER: [{self.mano_inicial_crupier[0]}][¿?]")
            #print(f"Cartas del CRUPIER: [{self.mano_inicial_crupier[0]}][{self.mano_inicial_crupier[1]}] y suman {sum(self.valor_cartas)}")
        
        #if (verificacion_mano.carta_visible_AS(self.mano_inicial_crupier)):
        #    return True

