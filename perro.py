#para crear un objeto 1 definimos su clase
#empieza siempre por mayusculas por convenio

class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):#el primer parámetro siempre hay que introducirlo
        #puede tener cualquier nombre pero por convenio se pone self
        if self.peso == None:
            print("soy un perro fantasma")
            return
            
        if self.peso >= 8:
            print ("GUAU, GUAU, GUAU")
        else:
            print("ay, ay, ay")

class Perro():
    def __init__(self, n, edad, p):
        self.nombre = n
        self.edad = edad
        self.peso = p
    
    def ladrar(self):#el primer parámetro siempre hay que introducirlo
        #puede tener cualquier nombre pero por convenio se pone self
        if self.peso >= 8:
            print ("GUAU, GUAU, GUAU")
        else:
            print("guau, Guau")
            
    def __str__(self):
        return "Soy el perro {}, tengo {} años y peso {} kilos".format(self.nombre, self.edad, self.peso)
    #con esto defino la cadena que me devuelve si pongo
    #print(salchico) por ejemplo en vez de devolver
    #<__main__.Perro object at 0x0403FD30>
    #devolveria "soy el perro "nombre", tengo "x" años y peso "x" kilos

#para probar en la shell
        #salchicho = Perro('salchicho', 3, 11)
        #lola = Perro('lola', 5, 3)
        #salchicho.ladrar()
        #lola.ladrar()
        #salchicho.peso
        #salchicho.edad = 7
        #etc
        
class PerroAsistencia(Perro):#hereda de la clase Perro, es una subclase
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False

    def __str__(self):
        return "Perro asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear".format(self.nombre, self.amo))
    
    def ladrar(self):
        if self.__trabajando:
            print("no puedo ladrar, estoy paseando")
        else:
            Perro.ladrar(self) #invocamos a la funcionalidad del padre
            #por eso ponemos Perro delante
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            

        
            
