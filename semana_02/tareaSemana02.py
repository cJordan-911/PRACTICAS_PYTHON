import math
# EJERCICIOS ACTIVIDAD SEMANA 02
# 1.Realizar un programa que ingrese sus datos personales e imprimirlos
print("INGRESE SUS DATOS PERSONALES")
nombre = input ("ingrese su nombre: ")
apellidos = input ("ingrese sus apellidos: ")
edad = input ("ingrese su edad: ")

print('Hola {} {}, su edad es {}'.format(nombre, apellidos, edad))

# 2.Calcule el área de un círculo con radio ingresado desde el teclado.
print("ÁREA DE UN CÍRCULO")
radio = int(input("ingrese el radio: "))
area= math.pi * (radio**2);
print('El área del círculo es {}'.format(area))

# 3.Ingrese 3 valores y realice las operaciones de suma ,resta y multiplicació
print("INGRESE 3 VALORES")
v1 = int(input ("ingrese primer valor: "))
v2 = int(input ("ingrese segundo valor: "))
v3 = int(input ("ingrese tercer valor: "))

suma= v1 +v2+v3
resta=v1-v2-v3
multiplicacion= v1 *v2*v3
print('La suma, resta y multiplicaión son {}, {}, {} respcetivamente'.format(suma, resta, multiplicacion))

# 4.Ingrese un valor e imprima el tipo de dato
print("INGRESE UN VALOR")
numero = int(input ("saber el tipo de dato de: "))
type= type(numero)

print('El tipo de dato es: {}'.format(type))

# 5. Realice un programa que imprima la ubicación de su carpeta donde se encuentra trabajando.
import sys
print ("ubicación es esta: ",sys.argv[0])

# 6.Realice un programa que calcule la suma de los números hasta el valor ingresado
print("SUMA DE NÚMERO N VECES")
cantidad = int(input ("ingrese cuántos valores quiere sumar: "))
numero=1
suma=0

while numero <= cantidad:
    valores = int(input ("ingrese otro valor: "))
    numero+=1
    suma+=valores
print('La suma final de los valores es: {}'.format(suma))

# 7. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
print("DETERMINAR")
valor1 = int(input ("ingrese el primer valor: "))
valor2 = int(input ("ingrese el segundo valor: "))

if valor1==valor2:
   print('son iguales')
else:
    print('son diferentes')
    if(valor1>valor2):
        print('y además el primero es mayor al segundo')
    else:
        print('y además el segundo  es mayor al primero')

# 8.Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
# usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
print("CONTRASEÑAS")
contrasenia = 'Raaa'
contrasenia_lowe = contrasenia.lower()

verficacion = str(input ("ingrese su contraseña: "))
verificacion_lower = verficacion.lower()
if(contrasenia_lowe==verificacion_lower):
    print("contraseña correcta");
else:
    print("contraseña incorrecta")

# 9.Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
print("PAR O IMPAR")

parImpar = int(input ("ingrese el número: "))

residuo= parImpar%2

if(residuo ==0):
    print("el número es par")
else:
    print("el número es impar")

# 10.Realizar un programa que calcule la penalidad por la mora de una deuda,sabiendo que si se
# demora de 1 día a 10 se le agrega el 5% , si se demora hasta 30 días se le agrega 8% y pasando
# el rango máximo se le agrega un 10%.
print("CALCULE MORA")

deuda=float(input('Ingrese el monto de la deuda: '))
mora=0.0
diasTardanza=int(input('Ingrese el días de tardanza: '))

if diasTardanza>0 and diasTardanza<=10:
    mora=0.05
elif diasTardanza>10 and diasTardanza<=30:
    tasa=0.08
else:
    mora=0.1

deudaAgregada=deuda*mora
print("su penalidad por mora es de S/.{} ".format(deudaAgregada))

# 11.Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú
print("MENU OPERACIONES")
numeeroOp1= int(input('Ingrese el primer número: '))
numeeroOp2= int(input('Ingrese el segundo número: '))
print('==================================')
print("1)Mostrar una suma de los dos números:\n2)Mostrar una resta de los dos números (el primero menos el segundo):\n3)Mostrar la multiplicación de los dos números:")
opcionElegida=int(input('Seleccione una opción: '))
print('==================================')

if opcionElegida == 1:
	print('La suma de ambos número es: {}'.format(numeeroOp1+numeeroOp2))
elif opcionElegida == 2:
	print('La resta de ambos número es: {}'.format(numeeroOp1-numeeroOp2))
elif opcionElegida == 3:
	print('La multiplicación de ambos número es: {}'.format(numeeroOp1*numeeroOp2))
else:
	print('opción incorrecta')

# 11.Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es
# vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle
# que no se puede procesar el dato.
print("ES VOCAL")
vocales=['a', 'e', 'i', 'o', 'u']

letra=str(input('Ingrese la letra: '))

if len(letra)>1:
    print('solo debe ingresar un caracter')
else:
    if letra in vocales:
        print ('la letra es una vocal')
    else:
        print('no es una vocal')

# 12.Defina una lista de 5 estudiantes realice lo siguiente :
print("JUGANDO CON LISTAS")
listaEstudiantes=['Carlos Jordan', 'Juanito Alcachofas', 'Monserrat de Monsefu', 'Juan Manolo', 'Piero Mateo']

tamanio_lista= len(listaEstudiantes)
ultimo_elemento= listaEstudiantes[-1]
lista_revertida= list(reversed(listaEstudiantes))

print('tamño lista: {}'.format(tamanio_lista))
print('ultimo elemento: {}'.format(ultimo_elemento))
print('lista revertida: {}'.format(lista_revertida))

# 13.Defina un diccionario con una tupla y una lista de elementos, modifique el ultimo elemento.
diccionarioTarea={
    "tupla": (1,1,1,2,3,4,5,6,[1,2,3],8,(1,2,3),'soy el ultimo'),
}
valores=diccionarioTarea['tupla']
print('La lista es : {}'.format(valores))

ultimo_elemento= valores[-1]

letra_a_reemplazar=str(input('Reemplazar la letra a reemplazar: '))
letra_reemplazadora=str(input('Reemplazar valor de reemplazo: '))

reemplazado= ultimo_elemento.replace(letra_a_reemplazar,letra_reemplazadora)


print('Nuevo valor: {}'.format(reemplazado))

# 14.Realice un Menú interactivo que tenga las opciones de saludar ,una operación matemática y salir.
print("MENU INTEREACTIVO")
print('EELECCIONE UNA OPCIÓN')
print('==================================')
print("1)Saludar:\n2)Operación matemática:\n3)salir\n")
opcionElegida=int(input('Seleccione una opción: '))
print('==================================')

if opcionElegida == 1:
	print('Hola, ya te saludé')
elif opcionElegida == 2:
    numero1_opcion=int(input('Escriba un número: '))
    print('El cuadrado del número es {}'.format(numero1_opcion**2))
elif opcionElegida == 3:
	print('Fin del programa')

# 15.iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.
nombres=['Juan', 'Carlos', 'Romeo', 'Manolo','Rubí']
edades=[31,3,23,8,28]

lista_nombre_edades=[[nombres[0], edades[0]], [nombres[1], edades[1]], [nombres[2], edades[2]], [nombres[3], edades[3]],[nombres[4], edades[4]] ]
print (lista_nombre_edades)
indices_mayores=[]
for numero in edades:
    # print("este elemento es iterado",numero)
    if numero > 18:
        indices= edades.index(numero)
        indices_mayores.append(indices)
        
print('Estos son los índices', indices_mayores)
listaFinal=[]
for indicesFinales in indices_mayores:
    
    listaFinal.append(lista_nombre_edades[indicesFinales] )

print('LOS MAYORES DE EDAD SON: {}'.format(listaFinal))