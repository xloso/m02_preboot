def normal(x):
    return x

normal = lambda x: x # igual a la funcion normal anterior.

# si la funcion va a ser utilizable usar funcion
# si solo la usas una vez en un proceso te
#defines una funcion anonima "lambda"

def cuadrado (y):
    return y * y

def sumaTodos(limitTo, f):
    # f va a contener la referencia a la funcion a realizar
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    
    return resultado

if __name__ == '__main__': #solo lo va a ejeecutar el print sin es "principal"
    #así no lo ejecuta siempre si llamo a esta funcion desde otro sitio
    
    print (sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))
else:
    print (__name__)
