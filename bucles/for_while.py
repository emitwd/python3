#Creamos la lista con 3 elementos [se inicia desde el 0]
# 10 ocupa elemento 0
# 15 ocupa elemento 1
# 20 ocupa elemento 2
lista = [10, 15, 20]

#imprime el tipo de dato
print(type(lista))

# podemos determinar cuanto va durar el bucle for de varias formas pero en este caso se hace con una lista
# el bucle for recorre la lista [lista]
# despues va guardando cada elemento de la lista en la variable [i] y la va imprimiendo
# cuando termina de imprimir cada elemento el bucle for termina ya que la lista se quedo sin elementos por recorrer
for i in lista:
    print(i)

#while funciona casi igual que for pero para que el bucle se inicie nesecita un valor bool [true o false]
on = True
while on:
    print("este mensaje se va repetir en bucle si la variable [on] nunca es cambiada a false")
    on = False