def maximo(*l): #l es un array que meteré separados por comas
    if len(l) == 0:
        return 0
    m = l[0]
    for indice in range(1, len(l)): #no empiezo por 0 porque antes ya he comprobado si había un cero
        if l[indice] > m:
            m = l[indice]
    return m

def minimo(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for indice in range(1, len(l)): #no empiezo por 0 porque antes ya he comprobado si había un cero
        if l[indice] < m:
            m = l[indice]
    return m

def media(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for valor in l: #no empiezo por 0 porque antes ya he comprobado si había un cero
        suma += valor
        
    return (suma / len(l))

funciones ={
    'max': maximo,
    'min': minimo,
    'med': media
}
#es un diccionario

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return None
    
'''
para probarlo en la shell
>>> returnF('max')
<function maximo at 0x03F00F18>
>>> returnF('max')(1,3,-1,15,9)
returnF('min')(1,3,-1,15,9)
15
'''
# ejecutar funciones sobre funciones muy útil en big data
#una funcion es de nivel superior si admite como parámetros
# funciones o su resultado es una funcion o ambas