"""
6 - Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

from colorama import Fore, Back

def inversa(texto):
    invertida = '';
    for i in reversed(texto):
        invertida += i;
    return invertida

print(Back.BLUE, "Invertir cadena de texto",Back.RESET)
print(Fore.WHITE, inversa(texto='estoy probando'), Fore.RESET)


def inversa2(texto):
    
    invertida = ''
    longitud = -len(texto)
    
    for (letra) in range(longitud, 1):
        letra = abs(letra)
        invertida += texto[letra - 1]
        
    return invertida

print(Back.MAGENTA, "Invertir cadena de texto 2", Back.RESET)
print(Fore.WHITE, inversa2(texto='estoy probando'), Fore.RESET)