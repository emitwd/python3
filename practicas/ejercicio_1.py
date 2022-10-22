"""
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

"""

def max(num1: int, num2: int):
    numeros = [num1, num2]
    if numeros[0] > numeros[1]:
        return numeros[0]
    else:
        return numeros[1]

print('Max de dos numeros');
print(max(30, 20));