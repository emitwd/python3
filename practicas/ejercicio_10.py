from colorama import Fore, Back  # Importa los estilos de color para la consola
from random import randrange  # Importa una función para generar números aleatorios
from os import system  # Importa la función para limpiar la pantalla

system('cls')  # Limpia la pantalla de la consola

# Imprime el encabezado del juego con un fondo de color magenta claro
print(Back.LIGHTMAGENTA_EX + "JUEGO EN PYTHON" + Back.RESET)

# Define las opciones del juego con colores para el texto
opciones = [f'\n{Fore.CYAN}Piedra - 0\n', f'{Fore.YELLOW}Papel - 1\n', f'{Fore.MAGENTA}Tijera - 2\n']

# Solicita al jugador que elija una opción e imprime las opciones disponibles
jugador = int(input(opciones[0] + opciones[1] + opciones[2] + Fore.RESET + '\n\n\n DIGITA UN NUMERO: '))
system('cls')  # Limpia la pantalla de la consola

maquina = randrange(3)  # Genera un número aleatorio para la elección de la máquina

# Define los resultados del juego con diferentes colores de fondo
resultados = ['EMPATE', 'PERDISTE', 'GANASTE']

# Imprime la elección de la máquina
print('MAQUINA: ' + opciones[maquina])

# Determina el resultado del juego y lo imprime con el color de fondo correspondiente
if (jugador - maquina) % 3 == 0:
    print(Back.YELLOW + resultados[0] + Back.RESET)  # Empate
else:
    print(Back.RED + resultados[(maquina - jugador) % 3] + Back.RESET)  # Gana o pierde según el resultado
