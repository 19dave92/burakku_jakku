import os
import keyboard
import colores as cs

def borrar_pantalla():
    print("Presione C para continuar...")
    while True:
       #event = keyboard.read_event(suppress=True): 
       # Esta línea lee un evento del teclado sin imprimirlo en la consola, 
       # gracias al argumento suppress=True. Esto nos permite detectar 
       # eventos del teclado sin mostrarlos al usuario.
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'c':
            os.system('cls' if os.name == 'nt' else 'clear')
            break        


def reglas_basicas():
    print(f"""
        {cs.subr(cs.bold("Valor de las cartas:"))}

Cada carta del 2 al 10 tiene su valor nominal:
    
                [2♥] = 2
                [3♦] = 3
                [4♣] = 4
                [5♠] = 5
                [6♦] = 6
                [7♣] = 7
                [8♠] = 8
                [9♦] = 9
                [10♥]= 10

Jotas(J), Reinas(Q) y Reyes(K) valen 10 puntos:

                [J♥] = 2
                [Q♦] = 3
                [K♣] = 4

El 'AS' se valora como 1 u 11 puntos, segun elijan 
los jugadores.

                [AS♥] = 11
                [AS♦] = 11
                [AS♣] = 11
                [AS♠] = 11
        
    """)
    
    borrar_pantalla()

    print(f"""   
                {cs.subr(cs.bold("Objetivo:"))}

El jugador pide cartas para alcanzar 21 san pasarse.

Hay Blackjack si el jugador tiene 21 puntos en la tirada inicial
        
                        [AS♥][J♠] = 21

El objetivo del jugador es vencer a la banca consiguiendo mas 
puntos que ella, o dejando que su puntuación supere los 21 puntos.

    """)
    
    borrar_pantalla()

    print(f"""
        {cs.subr(cs.bold("Acciones basicas:"))}

Pedir carta: La banca te da otra carta.

Plantarse: Plantate cuando tengas suficientes puntos y no quieras mas cartas.

Doble (x2): Dobla o duplica tu apuesta y consigue una carta mas.
""")
    
    borrar_pantalla()

    print(f"""
                {cs.subr(cs.bold("Cortador:"))}

Si las dos primeras cartas forman una pareja, el jugador
puede separarlas en dos manos distintas, apostando la misma
cantidad en ellas, y jugando de forma separada.

                       {cs.red("[10♥]")}{cs.black("[10♦]")}
                       apuesta: 100
                            | 
                            |
        {cs.red("[10♥]")}[8♣]      <<<<<|>>>>>      {cs.black("[10♦]")}[5♣]
        apuesta: 100                    apuesta: 100
""")
    
    borrar_pantalla()

    print(f"""
{cs.subr("Seguro:")}

Si la carta de la banca es un AS, el jugador puede asegurarse
a si mismo contra un blackjack, pagando la mitad de su apuesta
inicial.
Si la carta oculta de la banca es un 10 o una figura, el jugador
gana 2 contra 1.
Si la carta de la banca no es un 10, la apuesta asegurada se pierde.


Puedes leer el reglamento completo o jugar.
""")

def reglamento_completo():

    print(f"""
                            {cs.subr(cs.bold("Básicos del blackjack"))}

Para empezar, el blackjack es un juego de cartas donde el apostador competirá 
contra la casa o el crupier. El juego consiste en los jugadores sacando cartas 
que tienen un valor específico. Por ejemplo, todas las cartas de 2 a 10 tienen 
un valor basado en el número que aparece en la carta. Es decir, que un 5 de 
corazones tiene un valor de 5 y un 9 de picas tiene un valor de 9. Es importante 
tener en cuenta que el palo de la carta no tiene influencia en su valor. Eso 
quiere decir que un 4 de diamantes y un 4 de corazones tienen el mismo valor de 4.
Adicionalmente, todas las cartas de la corte: jotas, reinas y reyes del mazo 
tienen un valor de 10 cada una. El as es considerado la única carta diferente 
porque tiene dos valores, es decir, el as puede contarse como 11 o como 1 y esto 
lo determinará la combinación de cartas que el jugador tenga. Por ejemplo, si un 
jugador saca un as y un 9, entonces es probable que cuenten el as como un 11, 
dándole al apostador un conteo total de cartas de 20 (11+9).
Sin embargo, si el apostador saca un 3 y un as, pueden escoger que el as sea un 1 
y solicitarle al crupier una carta adicional (pedir).
El objetivo del juego de blackjack es lograr una puntuación lo más cerca posible 
del 21. Esto debe lograrse sin pasarse del 21. Si no llegas al 21, el objetivo del 
juego es conseguir una puntuación mayor a la del crupier. Por ejemplo, un apostador 
saca un 10 y un 8 y por esa razón su puntuación es de 18. El crupier tiene un 9 y 
un 8, es decir, su puntuación es de 17. En este ejemplo, la puntuación del apostador 
es mayor que la del crupier y está más cerca del 21, y por esa razón, el apostador 
gana. En términos más sencillos, el objetivo principal del juego de blackjack es 
conseguir un as y una carta con valor de 10 para llegar a una puntuación total de 21.""")

    borrar_pantalla()
    print(f"""

                                {cs.subr(cs.bold("Apuestas y ganancias"))}

Para poder jugar blackjack y para poder jugar una ronda, el apostador debe hacer 
una apuesta. En términos de ganancias, una mano ganadora de blackjack recibirá un 
pago de 1:1. Esto significa que si el jugador apuesta $20 y gana la mano, deberá 
recibir $40. Es decir, los $20 de su apuesta original y $20 de ganancias. Si un 
apostador saca una mano de “blackjack” en sus primeras dos cartas, es decir, un as 
y una carta con valor de 10, se le pagará al apostador 3:2. Por ejemplo, si el 
jugador apuesta $20 y saca una mano de blackjack, su pago será $50. En el blackjack, 
tan pronto como el jugador tiene una mano ganadora, se le paga inmediatamente. El 
único momento en que no recibirá su pago inmediatamente es cuando la carta boca arriba 
del crupier es un as o una carta de 10. La razón es que el crupier también tiene una 
mano de blackjack y ese turno se considera un empate. En este caso, al apostador se 
le devolverá la cantidad inicial que apostó.""")
    
    borrar_pantalla()
    print(f"""

                                  {cs.subr(cs.bold("Límites de mesa"))}

Los límites de mesa para el blackjack varían de casino en casino. En algunos casinos 
físicos los límites de las mesas empiezan con un mínimo de $5, mientras que los casinos 
online ofrecen manos de hasta $1. Además de esto, cada casino puede tener un máximo de 
apuesta que puede estar entre $50 y $50 000 (sí, esto es en el Caesar’s Palace en 
Las Vegas, el único casino hoy en día en tener una apuesta máxima de $50 000). La mayoría 
de las mesas de blackjack permiten hasta 6 jugadores y una vez empieza el juego, el crupier 
repartirá las cartas a los apostadores de izquierda a derecha. Cuando todos los apostadores 
tengan sus cartas, el crupier será el último en actuar en el juego de blackjack.""")
    
    borrar_pantalla()
    print(f"""

                                    {cs.subr(cs.bold("Modo de juego"))}

El juego de blackjack empieza con el apostador colocando su apuesta en la casilla o círculo
de apuesta frente a él. Es importante tener en cuenta que se ubican fichas de baja denominación
sobre las demás fichas, mientras que las fichas de mayor denominación se ubican debajo. Una vez 
todos los jugadores han hecho sus apuestas, el crupier indicará que no se aceptan más apuestas. 
El juego de blackjack empezará y las cartas serán repartidas.
Para empezar, el crupier repartirá una carta del zapato barajado para el primer jugador a su 
izquierda y continuarán hacia la derecha hasta que a todos los apostadores se les haya repartido 
una carta. El crupier también se repartirá una carta a él mismo. Estas cartas repartidas a los 
apostadores se dan boca arriba pero la primera carta del crupier está boca abajo, y solo las 
siguientes cartas están boca arriba. Antes de que el juego continúe, si la carta boca arriba del 
crupier es un as, los apostadores tienen la opción de comprar una apuesta segura que cuesta un 
50% del valor de la apuesta. Por ejemplo, si el apostador hizo una apuesta de $100, para asegurar 
su mano en contra del posible blackjack del crupier necesitará comprar una apuesta segura por $50. 
Si el crupier sí tiene un blackjack, el apostador perderá su apuesta inicial de $100 pero recibirá 
un pago de 1:1 por su cantidad asegurar, es decir, recibirá $100. Además, todas las demás manos 
no aseguradas que no sean blackjack serán automáticamente manos perdedoras y el crupier recogerá 
las apuestas de estos jugadores y la ronda acabará. Si un jugador también tiene blackjack, esto 
se llama empate y el jugador solo recibirá de vuelta su apuesta original y el turno acabará.
En el escenario anterior, si el crupier no tiene un blackjack, los apostadores que compraron la 
apuesta segura, perderán la cantidad del seguro y el crupier preguntará a cada apostador, de 
izquierda a derecha, qué acción quiere realizar. Basándose en las cartas repartidas, el apostador 
puede escoger solicitar otra carta (pedir) o pueden escoger no solicitar cartas adicionales 
(plantarse). Es importante tener en cuenta que los apostadores tienen una variedad de opciones de 
las que escoger cuando sus primeras 2 cartas han sido repartidas y la decisión que tomen en este 
momento debe hacerse teniendo en cuenta las otras cartas que tienen los demás apostadores en la 
mesa y el crupier.""")
    
    borrar_pantalla()
    print(f"""
          
¿Entonces cómo sabe un apostador cuándo debe plantarse o pedir? El apostador necesita evaluar el 
valor de su carta. En la mayoría de los casos, un apostador se planta cuando el valor de sus cartas
está entre 16 y 21. La mayoría de los jugadores también piden si tienen 11 o menos. Un apostador 
puede pedir otra carta todas las veces que quiera pero una vez sobrepasan el 21, la mano se ha 
pasado y el crupier retirará la apuesta de ese jugador. Además, cuando un apostador pide varias 
veces, esta decisión debe estar basada en la carta boca arriba del apostador.
Si un jugador decide plantarse, el crupier continuará de izquierda a derecha hasta que cada 
jugador haya completado su turno.
Una vez todos los jugadores han completado sus acciones, el crupier revelará su carta boca abajo 
para mostrar su puntuación. Si un crupier tiene menos de 17, deberá continuar sacando cartas hasta 
que llegue a 17 o más, sin pasarse de 21. Cuando el crupier llegue a 17 o más, se plantará y su 
puntuación se comparará con la de cada jugador. Si la puntuación del jugador es mayor que la del 
crupier, se les pagará 1:1 y si la puntuación es menor que la del crupier, entonces perderá su 
apuesta inicial. En el caso de que las puntuaciones del apostador y el crupier sean iguales, al 
apostador se le devolverá su apuesta inicial y se considerará un empate. Si el crupier se pasa en 
cualquier momento, todos los apostadores en la mesa ganan y recibirán pagos 1:1. Cualquier 
apostador que tuviera blackjack, ya se le ha debido pagar 3:2 durante la ronda.
Esta es la información básica sobre blackjack y cómo jugar este emocionante juego. Ahora pasaremos 
a hablar de reglas avanzadas e intermedias de blackjack donde se tocarán temas interesantes como 
doblar, dividir y más. Las reglas que hemos cubierto hasta ahora son la forma más pura de 
blackjack pero es importante tener en cuenta que existen variaciones. También hablaremos de esas 
formas de blackjack en otros tutoriales pero nunca debes olvidar que las reglas básicas del 
blackjack de las que hemos hablado aquí no cambiarán.
          
                                    {cs.subr(cs.bold("¡Listo para jugar y ganar!"))}
""")
    borrar_pantalla()