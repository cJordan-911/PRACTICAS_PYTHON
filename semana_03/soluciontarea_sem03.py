# 1.Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número.
iteracion = 0
while iteracion <= 8:
    iteracion+=1
    if(iteracion % 2 ==0):
        print('Este número es par: {}'.format(iteracion))

# 2. Realizar un programa que dibuje un cuadrado en consola con * ,usando bucles .
lado= int(input('Ingrese el lado del cuadrado: '))

for i in  range(1, lado+1):
    for j in range(1, lado+1):
        print(" * ", end='')
    print(" ")

# 3.Realizar un programa que dibuje un triángulo en consola con * ,usando bucle
triangulo = '*'
for i in range(6):
    print(triangulo * i)

# 4. Realizar un programa que inserte valores en una lista desde el 1 hasta el 100 saltando en 2 en 2 
for i in range (1,100,2):
    print (i)

# 5.Definir una función que multiplique 2 números mayores de cero.
def multiplicar(n1, n2):
    resultado=0
    if n1 <=0:
        mensaje= 'Debe ingresar un número mayor a 0 para valor 1'
        return print(mensaje) 
    else:
        if n2 <=0:
            mensaje= 'Debe ingresar un número mayor a 0 para valor 2'
            return print(mensaje) 
        else:
            resultado= n1*n2
            print("La multiplicacion es: {}".format(resultado))

num1= int(input('Ingrese primer valor: '))
num2 = int(input('Ingrese segundo valor: '))

multiplicar(num1, num2)

# 6 Definir las siguientes funciones :
# -saludar(nombre)
# -realizarTarea(tarea)
# -despedirse(nombre)
# *las funciones imprimen lo que se envía como parámetro
def saludar(param_nombre):
    print('Hola cómo estás: {}'.format(param_nombre))
def realizarTarea(param_tarea):
    print('Estás realizando la tarea: {}'.format(param_tarea))
def despedirse(param_despido):
    print('Adios manito: {}'.format(param_despido))

saludo = str(input('Ingrese su nombre para saludarlo: '))
tarea = str(input('Ingrese la tarea a realizar: '))
despido = str(input('Ingrese su nombre para despedirlo: '))

def mensajes(saludo_p, tarea_p, despido_p):
    print('**********************')
    saludar(saludo_p)
    realizarTarea(tarea_p)
    despedirse(despido_p)
    print('**********************')

mensajes(saludo, tarea, despido)

# 7 Definir una función que retorne el mayor valor al ingresar 2 números.
def comparar(n1, n2):
    if n1<=n2:
        print('**********************')
        print('el mayor numero es ', n2)
    else:
        print('**********************')
        print('el mayor numero es ', n1)

numero1=input('ingrese primer numero ')
numero2=input('ingrese segundo numero ')
 
comparar(numero1,numero2)

# 8. Definir una función que imprima los argumentos ingresados desde linea de comandos
# Nota: Usar import sys.argv => *args

import sys

def posicion(*args):
    for arg in args:
        print("Mira esto: ",arg)


posicion(sys.argv)

# 9.Realizar una función que tenga por parámetro un lista de numerosy aumente cada
# elemento en +1
lista=[1,2,3,4,5]

def aumentarLista(li):
    # print(li)
    for i in li:
        li[i-1]+=1

aumentarLista(lista)
print("Lista aumentada: ",lista)


# 10.Realizar un programa que realice las siguientes funciones de string al texto.
# -split
# -count
# -find
# -uppercase
# -lowercase
# texto=”Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
# Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
# impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y
# los mezcló de tal manera que logró hacer un libro de textos especimen.”
texto= 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.'

funcion_split = texto.split()
funcion_count = texto.count('Lorem')
funcion_find = texto.find('Ipsum')
funcion_upper = texto.upper()
funcion_lower = texto.lower()

print(funcion_split)
print(funcion_count)
print(funcion_find)
print(funcion_upper)
print(funcion_lower)


# 11.Definir los atributos y métodos de una de las siguientes clases.
# - Persona
# - Gato
# - Producto

class Gato:
    pass

gurrumino =  Gato()

gurrumino.patas = 'esponjosas'
gurrumino.ojos = "marrones"
gurrumino.pelaje = 'blanco'

print("Mi gato gurrumino tiene patas {}, ojos color {} y pelaje {}".format(gurrumino.patas, gurrumino.ojos, gurrumino.pelaje))



class Producto:
    pass

producto =  Producto()

producto.precio = 'S/.20'
producto.marca = "Ace"
producto.cantidad = '5'

print("Compré {} productos, de la marca {} y me costó {}".format(producto.cantidad , producto.marca, producto.precio))


class Persona:
    pass

persona =  Persona()

persona.nombre = 'Carlos Jordan'
persona.nota = '05'
persona.edad = 22

print("{} de {} años sacó {} en su práctica por presentar a destiempo, pero el profesor lo perdonó y lo aprobó con nota máxima.".format(persona.nombre , persona.edad, persona.nota))
