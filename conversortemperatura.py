class Termometro():
    def __init__(self):
        self.__unidadM = 'C' #al ponerlo con __ decimos que es privado
        # al ser privados tenemos que hacer setter y getter porque no vienen de fuera
        self.__temperatura = 0
    
    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidadM)

    def __conversor(self, temperatura, unidad):
        # es privada porque nadie tiene porqué saber como se hace
        if unidad == 'C':
            return "{}º F".format(temperatura * 1.8 + 32)
            
        elif unidad == 'F':
            return "{}º C".format((temperatura-32) / 1.8)
        else:
            return "unidad incorrecta"

#ahora hago un setter y un getter
    
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == "F" or uniM == "C":
                self.__unidadM = uniM
                
    def temp(self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM=None): #tenemos la unidad como opcional
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__() #se puede omitir el (self) entre los paréntesis