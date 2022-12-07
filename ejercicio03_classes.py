######
class Customer:
    edad=0
    def __init__(self,name,dni):
        self.name=name
        self.dni=dni
    def nameSpace(self):
        print(self.name)
    def __str__(self):
        return f'se llama {self.name}'
    def callEdad(self,edad):
        self.edad=edad
    def correo(self,correo):
        self.correo=correo

c1=Customer("gian","16467979")
# c1.nameSpace()
# print(c1.name)
# print(c1)
# print(type(c1))
####################

# __ -> inidica que es privado(de la clase)
class Animal:
    def __init__(self,name, especie) :
        self.name=name
        self.especie=especie
    def signoZodiacal(self):
        print(self.name)

animal= Animal('Gurrumino', 'Gato')
# signo= Animal('TAURO')
print(animal.especie)
# print(animalss)
# print(signo)
animal.signoZodiacal()