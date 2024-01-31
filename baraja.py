from random import random,choices
import main as ppal

baraja = {'2♥':2,'3♥':3,'4♥':4,'5♥':5,'6♥':6,'7♥':7,'8♥':8,'9♥':9,'10♥':10,'J♥':10,'Q♥':10,'K♥':10,'AS♥':10,
          '2♦':2,'3♦':3,'4♦':4,'5♦':5,'6♦':6,'7♦':7,'8♦':8,'9♦':9,'10♦':10,'J♦':10,'Q♦':10,'K♦':10,'AS♦':10,
          '2♣':2,'3♣':3,'4♣':4,'5♣':5,'6♣':6,'7♣':7,'8♣':8,'9♣':9,'10♣':10,'J♣':10,'Q♣':10,'K♣':10,'AS♣':10,
          '2♠':2,'3♠':3,'4♠':4,'5♠':5,'6♠':6,'7♠':7,'8♠':8,'9♠':9,'10♠':10,'J♠':10,'Q♠':10,'K♠':10,'AS♠':10}


def mano_inicial():
    jugador = choices(list(baraja), k=2)
    crupier = choices(list(baraja), k=2)
    return [jugador,crupier]  

def pedir_jugador():
    nueva_carta = choices(list(baraja), k=1)
    return nueva_carta[0]

def pedir_crupier(suma_crupier):

    nueva_carta = choices(list(baraja), k=1)
    
    print("El crupier pide carta") 
    
    ppal.inicial[1].append(baraja.pedir_crupier())
    
    suma_crupier = suma_crupier + baraja.baraja[ppal.inicial[1][-1]]
    
    print(f"La mano actual del crupier es [{ppal.inicial[1]} y suma {suma_crupier}") 

    return nueva_carta[0]
#print(pedir())
