import colores as estilo_texto

def splash_de_inicio():
    print(
"""
██████╗░██╗░░░██╗██████╗░░█████╗░██╗░░██╗██╗░░██╗██╗░░░██╗  ░░░░░██╗░█████╗░██╗░░██╗██╗░░██╗██╗░░░██╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░██╔╝██║░██╔╝██║░░░██║  ░░░░░██║██╔══██╗██║░██╔╝██║░██╔╝██║░░░██║
██████╦╝██║░░░██║██████╔╝███████║█████═╝░█████═╝░██║░░░██║  ░░░░░██║███████║█████═╝░█████═╝░██║░░░██║
██╔══██╗██║░░░██║██╔══██╗██╔══██║██╔═██╗░██╔═██╗░██║░░░██║  ██╗░░██║██╔══██║██╔═██╗░██╔═██╗░██║░░░██║
██████╦╝╚██████╔╝██║░░██║██║░░██║██║░╚██╗██║░╚██╗╚██████╔╝  ╚█████╔╝██║░░██║██║░╚██╗██║░╚██╗╚██████╔╝
╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░

                                    乃ㄩ尺闩长长ㄩ 丿闩长长ㄩ
""")
    print(f"""
Bienvenido a la mesa jugador, estas por comenzar a jugar Blackjack contra la banca.
Aqui no hay dinero real ni formas de adquirir dinero extra una vez tus fichas lleguen a cero.
La idea es que te diviertas en este juego desarrollado en Python. Cualquier bug que encuentres
por favor reportalo.

Si no conoces las reglas puedes {estilo_texto.subr("tipear o escribir")} {estilo_texto.green('REGLAS')} para acceder a ellas o puedes 
{estilo_texto.subr("tipear o escribir")} {estilo_texto.green('JUGAR')} para comenzar.
""")
        
    
