def normal(x):
    return x

def cuadrado (y):
    return y * y

def cubo(x):
    return x**3

def sumaTodos(limitTo, f):
    # f va a contener la referencia a la funcion a realizar
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    
    return resultado

print (sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))
