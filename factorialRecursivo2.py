"""
Simple código que devuelve el factorial de un numero dado
Para calcular dicho valor, hay que multiplicar el numero dado, por su
antecesor mientas sea superior a 1
Ejemplo del factorial de 5 seria:

    5 * 4 * 3 * 2 * 1  = 120
"""

def factorialRecursivo(n):
    if n>0:
        return n * factorialRecursivo(n-1)
    else:
        return 1


control = True
while control == True:
    try:
        n = int(input("numero para calcular el factorial: "))
        print("el factorial de {} es: {}".format(n, factorialRecursivo(n)))
        control = False
    except:
        print ("tiene que ser un numero entero")
        control = True