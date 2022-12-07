import ejercicio02_clase04
import ejercicio03_clase04

# 02. MOSTRANDO FUNCIÓN EJERCICIO 02
print('______________________')
print('SOLUCIÓN EJERCICIO 02')
ejercicio02_clase04.listarCatalogo()


# 03. MOSTRANDO FUNCIÓN EJERCICIO 03
print('______________________')
print('SOLUCIÓN EJERCICIO 03')
ejercicio03_clase04.Ladrar()
ejercicio03_clase04.Maullar()

# 04. MOSTRANDO FUNCIÓN EJERCICIO 04
print('______________________')
print('SOLUCIÓN EJERCICIO 04')
import os
os.system('echo "1era FUNNCION: Aquí usamola librería os con el método system, donde pondemos imprimir valor en consola"')
print('2da FUNNCION: Usaremos acá librería os para imprimir la ruta actual del proyecto: ',os.getcwd ())
print ("3era FUNNCION: Directorios existentes en la carpeta de la ruta actual son: %s"%os.listdir(os.getcwd()))


# 05. IMPRIMIR  EL NOMBRE DE ARCHIVO EJECUTADO
print('______________________')
print('SOLUCIÓN EJERCICIO 05')
print("Nombre del archivo que se ejecuta es : {}" .format(__name__))


# 06. NÚMEROS ALEATORIOS ENTRE EL 1 AL 100
print('______________________')
print('SOLUCIÓN EJERCICIO 06')
import random
for x in range(1): 
    print ('El número aleatorio entre el 1 y 100 es: ',random.randint(1,100))

# 07. NÚMEROS ALEATORIOS ENTRE EL 1 AL 100
print('______________________')
print('SOLUCIÓN EJERCICIO 07')


# 08. BUSCAR
print('______________________')
print('SOLUCIÓN EJERCICIO 08')

textoPython= 'Python es uno de los lenguajes de programación dinámicos más populares que existen entre los que se encuentran Java, Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje "scripting", es realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo, desde simples "scripts", hasta grandes servidores web que proveen servicio ininterrumpido 24×7. Es utilizado para la programación de interfaces gráficas y bases de datos, programación web tanto en el cliente como en el servidor (véase Django o Flask) y "testing" de aplicaciones'
palabra='Python'

if palabra in textoPython:
    print('Sí está incluido')