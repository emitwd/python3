"""
5 - Escribir una función sum() y una función multip()
que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

numeros=[1, 2, 3, 4]

def suma():
    resultado = 0;
    for i in numeros:
        resultado += i;
    return resultado

print("Suma de numeros de una lista")
print(suma())

def multiplicar():
    resultado = numeros[0];
    for i in numeros:
        resultado *= i;
    return resultado

print("Multiplicacion de numeros de una lista")
print(multiplicar())