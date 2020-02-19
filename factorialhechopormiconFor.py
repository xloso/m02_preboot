def factorial (x):
    
    total = 1
    
    for num in range(2, x+1):
        total = total * num
    return total

def factorialRecursivo(n):
    if n>0:
        return n * factorialRecursivo(n-1)
    else:
        return 1
    
numero = int(input("introduce número factorial: "))
print("el factorial con for de {}, es {}".format(numero, factorial(numero)))
print("el factorial recursivo de {}, es {}".format(numero, factorialRecursivo(numero)))        