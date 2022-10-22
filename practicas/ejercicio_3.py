"""
3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla 
por nosotros mismos resulta un muy buen ejercicio.
"""

lista = [10, 10, 20, 10]
def calcular_lista():
    numero = 0;
    for i in lista:
        numero += 1;
    return numero

print("Calcula casillas de lista")
print(calcular_lista())