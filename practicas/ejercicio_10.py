"""
JUEGO DE PIEDRA, 
PAPEL Y TIJERA
"""
from colorama import Fore, Back
from random import randrange
from os import system

system('cls')

while True:

    print(
        Back.LIGHTMAGENTA_EX+"JUEGO EN PYTHON"+Back.RESET
    )

    opciones = [
        
        f'\n{Fore.CYAN}Piedra - 0 \n', 
            f'{Fore.YELLOW}Papel - 1 \n', 
                f'{Fore.MAGENTA}Tijera - 2\n'
                
        ]
    
    jugador = int(input(opciones[0] + opciones[1] + opciones[2] + Fore.RESET +'\n\n\n DIGITA UN NUMERO: '))
    system('cls')
    maquina = randrange(0, 3)
    
    """
    0 PIEDRA
    1 PAPEL
    2 TIJERA
    """
    ganaste = Back.GREEN+'GANASTE'+Back.RESET
    perdiste = Back.RED+'PERDISTE'+Back.RESET
    empate = Back.YELLOW+'EMPATE'+Back.RESET
    print('MAQUINA: '+opciones[maquina])
    
    if jugador == 0 and maquina == 1: print(perdiste);
    elif jugador == 0 and maquina == 2: print(ganaste);
    elif jugador == 1 and maquina == 0: print(ganaste);
    elif jugador == 1 and maquina == 2: print(perdiste);
    elif jugador == 2 and maquina == 0: print(perdiste);
    elif jugador == 2 and maquina == 1: print(ganaste);
    elif jugador == maquina: print(empate);

    break
    