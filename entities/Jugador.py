import modules.baraja as mazo
from random import choices
#import verificacion_mano as vm

class Jugador():

    def __init__(self, nombre, fichas=50, hand=[]):
       
        self.nombre_jugador = nombre
        self.fichas_jugador = fichas
        self.hand = hand
        self.suma_mano_inicial = 0      # Inicializamos la variable que suma la mano total del jugador. Al ser un jugador nuevo la suma es cero.
        self.apuesta_segura = 0         # Inicializamos la variable que indica cuanto apuesta el jugador. Depende si gana o no, sumará o descontará de las fichas totales.
        print(f"Bienvenido a la mesa {self.nombre_jugador}, tienes un total de {self.fichas_jugador} fichas.\n")



    def apuesta(self):
        while True:
            try:
                self.monto_apostado = int(input(f"Por favor {self.nombre_jugador}, haga su apuesta: "))
            except:
                print("Por favor, ingresa un numero entero.")
            else: # <--- Se ejecuta si paso el try
                if (self.monto_apostado == 0):
                    print("No puedes apostar 0 (cero) fichas.")
                elif (self.monto_apostado > self.fichas_jugador):
                    print(f"No puedes apostar mas de lo que tienes. Recuerda que tienes {self.fichas_jugador} fichas")
                else:
                    self.fichas_jugador -= self.monto_apostado
                    break
           
        print(f"Has apostado {self.monto_apostado} fichas.")



    def mano(self, hand):

        #Almacen la mano de cada jugador
        self.hand = hand

        #Para sumar el valor de cuando pide una carta
        #suma_cartas_jugador += mazo.baraja[self.hand[-1]]

        #sumar el total de la mano
        self.suma_mano_inicial = [mazo.baraja[self.hand[0]],mazo.baraja[self.hand[1]]]            
        
        # if (sum(self.suma_mano_inicial) > 21 and self.contiene_as()):
        #     suma_cartas_jugador -= 10

        print(f"Cartas de {self.nombre_jugador}: [{self.hand[0]}][{self.hand[1]}] y suman {sum(self.suma_mano_inicial)}")

        #if (vm.contiene_AS(self.hand) == True and vm.contiene_FIGURA(self.hand) == True):
        #    print(f"Cartas de {self.nombre_jugador}: [{self.hand[0]}][{self.hand[1]}] - BURAKKU JAKKU")
        #else:
        #    print(f"Cartas de {self.nombre_jugador}: [{self.hand[0]}][{self.hand[1]}] y suman {sum(self.suma_mano_inicial)}")





"""

    def doblar_apuesta(self):
        self.monto_apostado *= 2
        print(f"Apuesta duplicada. Monto apostado: {self.monto_apostado}")

    def pide_carta(self):
        #Asigna una nueva carta al jugador
        nueva_carta = choices(list(mazo.baraja), k=1)
        self.hand.append(nueva_carta)
        print(self.hand)

    def plantarse(self):
        pass

    def asegurar(self):
        #el monto apostado + la mitad del monto apostado > cantidad de fichas
        if (self.monto_apostado + (self.monto_apostado // 2) < self.fichas_jugador):
            while True:
                print("¿Asegurar apuesta?\n      [1] Si\n        [2] No")
                try:
                    decision_jugador = int((input(">>> ")).strip())
                except:
                    print("Por favor ingrese 1 o 2")
                else:
                    break
            if (decision_jugador == 1):
                self.apuesta_segura = self.monto_apostado // 2

###################################################################################
######################__PREMIOS__##################################################

    def pagar_simple(self):
        self.fichas_jugador = self.fichas_jugador + (self.monto_apostado * 2)
        print(f"Se paga comun, obtiene {self.monto_apostado}. El jugador {self.nombre_jugador} tiene {self.fichas_jugador}")
    
    def pagar_bj(self):
        self.fichas_jugador = round(self.fichas_jugador + (self.monto_apostado * 2.5))
        print(f"Se paga BJ, obtiene {self.monto_apostado * 1.5}. El jugador {self.nombre_jugador} tiene {self.fichas_jugador}")

###################################################################################
######################__PERDIDA__##################################################
      
    def jugador_pierde(self):
        
        self.fichas_jugador -= self.monto_apostado
        print(f"La casa gana. {self.nombre_jugador} te quedan {self.fichas_jugador} fichas.")

        if (self.fichas_jugador == 0):
            print(f"{self.nombre_jugador} te has quedado sin fichas. Gracias por jugar.")
            #TODO: Destruir el objeto o el jugador.      
        else:
            print(f"Te quedan {self.fichas_jugador} fichas.")

###################################################################################
###################################################################################
            

###################################################################################___PRUEBAS

#david = Jugador('david')

#hand = ['AS♥', '8♥']

#david.mano(hand)

#print(sum(david.suma_mano_inicial))

#david.apuesta()

#david.doblar_apuesta()

#david.pagar_bj()

"""