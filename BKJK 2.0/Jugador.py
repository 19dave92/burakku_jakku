import baraja as mazo
import verificacion_mano as vm

class Jugador():
    

    def __init__(self, nombre, fichas=50):
        self.nombre_jugador = nombre
        self.fichas_jugador = fichas
        print(f"Bienvenido a la mesa {self.nombre_jugador}, tienes un total de {self.fichas_jugador}.")

    def mano(self, hand):
        #Almacen la mano de cada jugador
        self.hand = hand
        #Para sumar el valor de cuando pide una carta
        #suma_cartas_jugador += mazo.baraja[self.hand[-1]]

        #sumar el total de la mano
        suma_cartas_jugador = mazo.baraja[self.hand[0]] + mazo.baraja[self.hand[1]]
        
        #if (suma_cartas_jugador > 21 and self.contiene_as()):
        #    suma_cartas_jugador -= 10
        if (vm.contiene_as(self.hand) == True and vm.contiene_figura(self.hand) == True):
            print(f"Cartas de {self.nombre_jugador} son: [{self.hand[0]}][{self.hand[1]}] - BURAKKU JAKKU")
        else:
            print(f"Cartas de {self.nombre_jugador} son: [{self.hand[0]}][{self.hand[1]}] y suman {suma_cartas_jugador}")
        
###################################################################################
######################__PREMIOS__##################################################

    def apuesta(self):
        while True:
            try:
                self.monto_apostado = int(input(f"{self.nombre_jugador} haga su apuesta: "))
                if (self.monto_apostado == 0):
                    print("No puedes apostar 0 (cero) fichas.")
                    #TODO: Intentar agregar una excepcion personalizada
                elif (self.monto_apostado > self.fichas_jugador):
                    print(f"No puedes apostar mas de lo que tienes. Recuerda que tienes {self.fichas_jugador} fichas")
                else:
                    break
            except:
                print("Por favor, ingresa un numero entero.")

        print(f"Ha apostado {self.monto_apostado} fichas.")
    
    def pagar(self):
        self.fichas_jugador = self.fichas_jugador + self.monto_apostado
        print(f"Se paga comun. El jugador {self.nombre_jugador} tiene {self.fichas_jugador}")
    
    def pagar_bj(self):
        self.fichas_jugador = round(self.fichas_jugador + (self.monto_apostado * 2.5))
        print(f"Se paga BJ. El jugador {self.nombre_jugador} tiene {self.fichas_jugador}")
    
    
    def jugador_pierde(self):
        
        self.fichas_jugador -= self.monto_apostado
        print(f"La casa gana. {self.nombre_jugador} te quedan {self.fichas_jugador} fichas.")

        if (self.fichas_jugador == 0):
            print(f"{self.nombre_jugador} te has quedado sin fichas. Gracias por jugar.")
            #TODO: Destruir el objeto       
        else:
            print(f"Te quedan {self.fichas_jugador}.")


###################################################################################
