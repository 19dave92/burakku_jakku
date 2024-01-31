from colorama import init, Fore, Back, Style

init()

red =       lambda cadena: Fore.RED     + cadena + Fore.RESET
black =     lambda cadena: Fore.BLACK   + cadena + Fore.RESET
blue =      lambda cadena: Fore.BLUE    + cadena + Fore.RESET
cyan =      lambda cadena: Fore.CYAN    + cadena + Fore.RESET
green =     lambda cadena: Fore.GREEN   + cadena + Fore.RESET
mag =       lambda cadena: Fore.MAGENTA + cadena + Fore.RESET
yellow =    lambda cadena: Fore.YELLOW  + cadena + Fore.RESET

subr = lambda cadena: "\033[4m"+ cadena +"\033[0m"

bold =   lambda cadena: Style.BRIGHT + cadena + Style.RESET_ALL
