class Termometro():
    def __init__(self):
        self.__unidadM = 'C' #al ponerlo con __ decimos que es privado
        self.__temperatura = 0
    
    def conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 1.8 + 32)
            
        elif unidad == 'F':
            return "{}º C".format((temperatura-32) / 1.8)
        else:
            return "unidad incorrecta"
    
    def __str__(self):
        return "{}º {}".format(self.temperatura, self.unidadM)
    
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
        if uniM == None or uniM == self.unidadM:
            return selt.__srt__(self)
        else:
            return self.conversor(self.temperatura, self.__unidadM)