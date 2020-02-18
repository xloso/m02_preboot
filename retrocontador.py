def retrocontador(e):
    print("{},".format(e), end="") # el end es para que no haya salto linea
    if e>0: #tiene que haber alguna condicion para que no entre en bucle infinito
        retrocontador (e-1)
    #esto es una función recursiva
    
retrocontador(10)

    