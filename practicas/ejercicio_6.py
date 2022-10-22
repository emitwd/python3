"""
6 - Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(texto):
    invertida = '';
    for i in reversed(texto):
        invertida += i;
    return invertida

print("Invertir cadena de texto")
print(inversa(texto='estoy probando'))
