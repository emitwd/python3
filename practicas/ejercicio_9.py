"""
VER SI UNA CADENA DICE LOS MISMO
DE INICIO A FIN Y DE FIN A INICIO

EJEMPLO: Luz azul
"""


def es_palindromo(cadena = str()):
    
    longitud = -len(cadena)
    invertida = str()
    
    for letra in range(longitud, 0):
        invertida += cadena[abs(letra)-1]
        
        #LOS ESPACIOS DEBERIAMOS QUITARLOS PARA PODER SEGUIR CON LA COMPARACION
        #IGUAL TENEMOS QUE HACER LA COMPARACION CON CAPITALIZE PARA QUE DE IGUAL LAS MAYUSCULAS
    cadena1=cadena.capitalize().replace(' ', '')
    cadena2=invertida.capitalize().replace(' ', '')
    
    if cadena1 == cadena2:
        return True
    
    return False

print(es_palindromo('luz azul'))

