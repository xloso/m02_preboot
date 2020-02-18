from functools import reduce

def doble(x):
    return x+x

lista = [1, 3, -1, 15, 9]


listaDobles = map(lambda x: x*2, lista)
#map realiza la operacion en cada elemento de la lista
listaDobles1 = map(doble, lista)


def esPar(x):
    return x % 2 == 0


listaPares = filter(lambda x: x%2 ==0, lista)
#los pares, me filtra los que el resto de dividir por 2 sea cero
#filter devuelve verdadero o falso y en consecuencia hacemos
listaPares1 = filter(esPar, lista)

#reduce procesa 1 por 1 los valores y los transforma en 1 valor
#reduce reduce todo a 1 solo valor que será la operación
# a realizar según la función
#la X representa el valor que va a devolver el reduce
# la Y representa los valores de la lista.
sumatorio = reduce(lambda x, y : x+y, lista)

suma100 = reduce(lambda x,y: x+y, range(101))

sumatorioDobles = reduce (lambda x,y: x+y*2, lista)

print(list(listaPares))
print(list(listaPares1))
print(sumatorio)
print(sumatorioDobles)
print(suma100)

