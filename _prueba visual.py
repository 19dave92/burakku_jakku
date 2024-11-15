import colores

lista = [[['8♦', '7♦'],['K♠', '3♥'],['Q♠', '2♦'],['K♣', '9♦'],['10♣', '5♠'],['9♠', 'Q♥'],['K♠', 'AS♥']], ['3♦', 'K♠']]

lista2 = [['8♦', '7♦'],['K♠', '3♥'],['Q♠', '2♦'],['K♣', '9♦'],['10♣', '5♠'],['9♠', 'Q♥'],['K♠', 'AS♥'], ['3♦', 'K♠']]

print(f"""
      
                                          crupier
                                        {colores.bold(colores.red(str(lista[0][2])))}
apuesta: 10                                                                    apuesta: 10         
{colores.red(f"[{lista[0][0][0]}][{lista[0][0][1]}]")} apuesta: 10                                         apuesta: 10 {colores.mag(str(lista[0][6]))}
 jugador_1   {colores.blue(str(lista[0][1]))} apuesta: 10               apuesta: 10 {colores.cyan(str(lista[0][5]))}  jugador_7
               jugador_2  {colores.green(str(lista[0][2]))} apuesta: 10 {colores.yellow(str(lista[0][4]))}  jugador_6
                            jugador_3  {colores.black(str(lista[0][3]))}  jugador_5
                                         jugador_4
""")		

for i in lista2:
    if('K♠' in i == True):pass

lista3 = ['8♦', '7♦']
if '8♦' in lista3: print("Si esta")

for i in lista2:
    for x in range(2):
        'K' == i[x] 