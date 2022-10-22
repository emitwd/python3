"""
4 - Escribir una función que tome un carácter y devuelva True si es una vocal,
de lo contrario devuelve False.
"""

vocales = ['a', 'e', 'i', 'o', 'u']
def vocal(letra: str):
    if letra in vocales:
        return True
    else:
        return False

print("Si la letra es una vocal")
print(vocal(letra='a'))