#sumatorio recursivo

def sumatorio(n):
    if n>0:
       return n + sumatorio(n-1)
    else:
        return 0
    
sumatorio(4)

def factorial(n):
    if n>0:
        print("{},".format(n))

