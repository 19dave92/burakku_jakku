# Cómo se reparten las cartas
Nos ubicamos en el modulo:
~~~
./modules/baraja.py
~~~
Tenemos un diccionario _(baraja)_ que contiene como KEY el simbolo de la carta y como VALUE el valor numérico de la misma.

La funcion __mano_inicial(cant_jugadores: int)__ recibe como parámetro un número entero que determinará la cantidad de veces que debe realizarse el proceso, este numero es la cantidad de jugadores que van a jugar la partida.

Utilizaremos un generador o _"list compression"_ para generar una lista donde en cada iteración obtendremos con la función _"choices"_ dos elementos _(k=2)_ del diccionario _"baraja"_. Estos elementos obtenidos seran las KEY y se almacenarán en la variable "__cartas_repartidas__: list". 

El valor devuelto por la funcion __"mano_inicial(cant_jugadores: int)"__ sera una lista de listas y contendrá el siguiente formato:

~~~
#La posición 0 corresponde al jugador, mientras que la ultima posicion corresponde al crupier:

>>>     #Valor devuelto para 1 jugador + crupier
>>>     [
            ['8♥', 'K♥'],         #_Cartas Jugador 1 [0]
            ['8♥', '9♥']          #_Cartas Crupier   [1]
        ]
>>>
>>>     #Valor devuelto para 7 jugadores + crupier
>>>     [
            ['K♥', 'K♥'],         #_Cartas Jugador 1 [0]
            ['7♥', '9♥'],         #_Cartas Jugador 2 [1]
            ['8♥', 'J♥'],         #_Cartas Jugador 3 [2]
            ['9♥', 'K♥'],         #_Cartas Jugador 4 [3]
            ['Q♥', 'K♥'],         #_Cartas Jugador 5 [4]
            ['AS♥', 'J♥'],        #_Cartas Jugador 6 [5]
            ['9♥', '9♥'],         #_Cartas Jugador 7 [6]
            ['K♥', '8♥']          #_Cartas Crupier   [7]
        ]
~~~

Podemos decir entonces que el valor devuelto es una lista, donde cada elemento es una lista con los KEYs del diccionario _"baraja"_.
Cada KEY representa una cara para ese jugador. 

La variable que contiene la lista devuelta por la funcion __"mano_inicial"__ se llama __"cartas_repartidas"__.

# Llamada a la función __"mano_inicial(cant_jugadores: int)"__

La invocación se realiza desde el módulo __"main.py"__ una vez que el usuario ha elegido jugar. El argumento enviado es la cantidad de jugadores y está definida por la propiedad "len" del diccionario que contiene la cantidad de jugadores _(diccionario_jugadores)_. La propiedad "len" nos devuelve un número entero en el cual ya esta contemplado el crupier.

La variable que contiene el valor retonrado por la funcion __"mano_inicial(cant_jugadores: int)"__ se llama: __"mano_inicial"__ _(list)_. 

Hasta este punto, las cartas aún __NO SON ASIGNADAS__ a cada jugador en el hilo de ejecución principal. Lo que buscamos simplemente es ya tener preprarada la lista para luego asignarlas mediante iteracion a la instancia de cada jugador.

# Asignación de las cartas para cada jugador
Utilizaremos un "for" para recorrer la lista generada a partir del diccionario jugadores. (ver linea 31 del modulo "main.py) y para cada jugador buscamos el método "mano()" que recibe como argumento las cartas que le corresponden a ese jugador en formato de lista.

~~~
 
#"jugador_buscado" es el nombre de un jugador.

> jugador_buscado.mano(mano_inicial[indice]) 

#De forma práctica/visual sería:

> DAVID.mano(mano_inicial[indice])
~~~ 
Donde:
* __mano_inicial__: Es la lista con todas las cartas incluidas las del crupier
* __[indice]__: Es una variablede tipo entero definido como __"indice"__ en el módulo __main.py__ incializado en 0 (cero) y vincula de forma ordenada a cada jugador con el par de cartas que le toca. Se autoincrementa antes de continuar con la siguiente iteración.

Si fueran 3 jugadores (sin incluir el crupier):
~~~
Listado de jugadores: ["DAVID", "FLOR", "SEBA", "CRUPIER"]
Listado de cartas: [['K♥', 'K♥'], ['7♥', '9♥'], ['8♥', 'J♥'], ['9♥', 'K♥']]

Asignacion:
[                                    [
    ['K♥', 'K♥'], ----[indice: 0]---- "DAVID",
    ['7♥', '9♥'], ----[indice: 1]---- "FLOR",
    ['8♥', 'J♥'], ----[indice: 2]---- "SEBA",
    ['9♥', 'K♥']  ----[indice: 3]---- "CRUPIER"
]                                    ]
~~~

En cada iteración del ciclo for utilizamos el método __"mano(hand: list)"__ de la clase __"Jugador.py"__ que recibe como parámetro la lista (_mano_inicial[indice]_) con las dos cartas que le fueron repartidas al comienzo. Accedemos a este método a traves de la instancia del objeto jugador.

## Interactuando con la clase 'Jugador' y obteniendo la suma de las dos cartas recibidas

Dentro del método __"mano(hand: list)"__ llamamos al módulo __"baraja"__ cuyo alias es __"mazo"__ (para facilitar la lectura del código ya que tanto el módulo como el diccionario tienen el mismo nombre) y obtenemos los VALUES de cada carta, es decir, el número entero que representan y los almacenamos en formato de lista en la variable __"self.suma_mano_inicial"__, obtenemos entonces:

~~~
Para el primer jugador:

| Consulta de keys         Diccionario "baraja"       VALUES obtenidos
|
|    ['K♥', 'K♥'] --------> {..., 'K♥':10, ...} --------> [10,10]

__"self.suma_mano_inicial"__ = [10,10] 

Para el segundo:

    ['7♥', '9♥'] --------> {..., '7♥':7, ..., '9♥':9, ...} --------> [7,9]

Para n jugador:

    [carta,carta] ---> {..., 'carta':int, ..., 'carta':int, ...} ---> [int, int]    
~~~

Mediante un print de pantalla mostramos la suma con la función __"sum()"__ que envía como argumento una lista y nos permite sumar todos sus elementos retornando el resultado de la suma. Este valor NO SE ALMACENA en ninguna variable ya que la cantidad de cartas irá variando.

La baraja con los KEYS se almacena en la variable __"self.hand"__ dentro de la función __"mano(hand: list)"__ de la clase __"Jugador.py"__.

Entonces: 
* __self.hand__: Contiene las cartas (Keys) del jugador.
* __self.suma_mano_inicial__: Contiene el valor de cada carta.

