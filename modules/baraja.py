"""
Modulo encargado de gestionar las cartas
"""

from random import random,choices

#Baraja chica para pruebas
baraja = {'7♥':7,'8♥':8,'9♥':9,'10♥':10,'J♥':10,'Q♥':10,'K♥':10,'A♥':11}

#baraja = {'2♥':2,'3♥':3,'4♥':4,'5♥':5,'6♥':6,'7♥':7,'8♥':8,'9♥':9,'10♥':10,'J♥':10,'Q♥':10,'K♥':10,'A♥':11,
#          '2♦':2,'3♦':3,'4♦':4,'5♦':5,'6♦':6,'7♦':7,'8♦':8,'9♦':9,'10♦':10,'J♦':10,'Q♦':10,'K♦':10,'A♦':11,
#          '2♣':2,'3♣':3,'4♣':4,'5♣':5,'6♣':6,'7♣':7,'8♣':8,'9♣':9,'10♣':10,'J♣':10,'Q♣':10,'K♣':10,'A♣':11,
#          '2♠':2,'3♠':3,'4♠':4,'5♠':5,'6♠':6,'7♠':7,'8♠':8,'9♠':9,'10♠':10,'J♠':10,'Q♠':10,'K♠':10,'A♠':11}


def mano_inicial(cant_jugadores):
    """
    Se reparten las primeras dos cartas para todos los jugadores y el crupier.
    Se usa un generador (for) para repartir las cartas para los jugadores.    

    Args:
        cant_jugadores (int): Es un numero entero con la cantidad de jugadores actuales.

    Returns:
        list: Lista con las cartas repartidas a cada jugador. Cada posición contiene una lista con dos cartas.
    """
    
    cartas_repartidas = [choices(list(baraja), k=2) for x in range(cant_jugadores)] #choices(elementos_a_extraer, cantidad_de_elementos_a_extraer(K=?))
    
    return cartas_repartidas  


def pedir_jugador():
    """
    Llamamos a esta funcion cuando el jugador en su turno pide una carta, dicha carta se agrega a su mano actual. 
    """
    nueva_carta = choices(list(baraja), k=1)
    return nueva_carta[0]

"""
def pedir_crupier(suma_crupier):

    nueva_carta = choices(list(baraja), k=1)
    
    print("El crupier pide carta") 
    
    ppal.inicial[1].append(baraja.pedir_crupier())
    
    suma_crupier = suma_crupier + baraja.baraja[ppal.inicial[1][-1]]
    
    print(f"La mano actual del crupier es [{ppal.inicial[1]} y suma {suma_crupier}") 

    return nueva_carta[0]

"""
## Seccion de pruebas
