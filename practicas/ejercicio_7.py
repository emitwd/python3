"""
VERIFICAR SI UNA LISTA TIENE 
UN ELEMENTO EN COMUN CON OTRA LISTA
"""

def algo_en_comun(lista_1, lista_2):
    for (elemento) in (lista_1):
        if (elemento) in (lista_2): return True
    return False
        

print(algo_en_comun([10, 10, 5], [1, 1, 5]))