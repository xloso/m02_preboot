from functools import reduce

def doble(x):
    return x+x

def sumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
    
    return resultado

def sumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor*2
    
    return resultado

def productoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
        
    return resultado

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
l= lista[:]
#l es una copia de lista, un clon
# si hacemos l=lista, no hacemos copia
#l apuntaria a lista y si mofifico l, se modifica lista
#haciendo lista[:] no pasa eso porque hago un clon.
sumatorio = reduce(lambda x, y : x+y, lista)

suma100 = reduce(lambda x,y: x+y, range(101))

sumatorioDobles = reduce (lambda x,y: x+y*2, lista)
#aquí sale 53 y no 54 porque reduce no suma el primer valor

print(list(listaPares))
print(list(listaPares1))
print(sumatorio)
print(sumatorioDobles)
print(suma100)

