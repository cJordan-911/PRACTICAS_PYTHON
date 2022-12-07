# 03. Crear una clase Animal ,luego una clase Perro y gato que sean hijos de Animal ,el método
# de Sonido debe ser diferente

class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    
class Perro(Animal):
    def __init__(self):
        super().__init__( self)

    def ladrar(self, nombre, sonido_perro):
       print('El animal es {} y el sonido que emite es {}'.format(nombre, sonido_perro)) 
    

class Gato(Animal):
    def __init__(self):
        super().__init__( self)

    def maullar(self, nombre, sonido_gato):
       print('El animal es {} y el sonido que emite es {}'.format(nombre, sonido_gato)) 

perro= Perro()
def Ladrar():
    return perro.ladrar('Firulais', 'ladrido')
gato= Gato()

def Maullar():
    return gato.maullar('Gurrumino', 'maullido')