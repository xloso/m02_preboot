
def factorialWhile(x):
    count = 1
    z = 1
    while z <= x:
        count = count * z
        z = z + 1
    return count    


def factorialFor (n):
    f = 1
    for i in range (2, n+1):
    #hay que sumar 1 a n porque sino el for se queda en el anterior
        f = f*i
    return f

try:
    x = int(input("introduce un numero entero: "))
    print("el factorial con while de {} es {}".format(x,factorialWhile(x)))
    print("el factorial con for de {} es {}".format(x,factorialFor(x)))
    
except:
    print ("tiene que ser un entero")






