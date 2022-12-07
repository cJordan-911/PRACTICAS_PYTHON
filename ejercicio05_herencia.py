class Figura:
    def __init__(self,lados):
        self.lados=lados


class Cuadrado(Figura):
    def __init__(self, lados):
        super().__init__(lados)
    def area(self,base,altura):
        return base*altura

class Circulo(Figura):
    def __init__(self, lados):
        super().__init__(lados)
    def area(self,radio):
        return 3.14*radio*radio

class Triangulo(Figura):
    def __init__(self, lados):
        super().__init__(lados)

    def area(self,base,altura):
        return base*altura/2

# ____________
class Figura:
    def __init__(self,lados):
        self.lados=lados

# cuadrado=Cuadrado(4,2,3)
# print(cuadrado)


# ___
class Restaurante:
    
    def __init__(self,restuarante_name, cuisine_type):
        self.restuarante_name=restuarante_name
        self.cuisine_type=cuisine_type
        self.estado=False
    def describe_restaurant(self):
        mensaje=''
        print(mensaje +'El nombre del restaurante es: {}, y su cuisine: {}'.format(self.restuarante_name, self.cuisine_type)) 
    def open_restaurant(self):
        self.estado=True
        # print('El restaurante está abierto') 
    def mostrar_estado(self):
        if(self.estado):
            print('El restaurante está abierto', self.restuarante_name) 
        else:
            print('El restaurante está cerrado', self.restuarante_name) 

restaurante_1= Restaurante('Rockys', 'pollería')
restaurante_2= Restaurante('La mochila', 'cevichería')
restaurante_1.describe_restaurant()
restaurante_1.open_restaurant()

restaurante_1.mostrar_estado()
restaurante_2.mostrar_estado()

# print(restaurante)

import saludar_archivo

saludar_archivo.saludar()
print('ACÁA')
saludar_archivo.nameFile()
print(__name__)

if __name__=='__main__':
    print('name')


# ->otra forma de inportar
# from saludar_archivo import *
# saludar()
    

