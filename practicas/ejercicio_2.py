"""
2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""
def max_de_tres(num1: int, num2: int, num3: int):
    numeros = [num1, num2, num3]
    if ( numeros[0] > numeros[1] and numeros[0] > numeros[2] ): return numeros[0];
    elif ( numeros[1] > numeros[0] and numeros[1] > numeros[2] ): return numeros[1];
    elif ( numeros[2] > numeros[0] and numeros[2] > numeros[1] ): return numeros[2];
    else: return 'Los numeros son iguales'

print('Max de tres numeros');
print(max_de_tres(50, 40, 30));