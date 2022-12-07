# 02.Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
# clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
# tener un método para agregar productos y otra para mostrar toda la lista de productos.

class Productos:
    # Constructor de clase
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria        

    def __str__(self):
        return 'La autoparte {} cuesta {} y pertenece a la categoría de {}'.format(self.nombre, self.precio, self.categoria)

productoInicial= Productos('Limpia parabrisas', 'S/. 200', 'limpieza')
# print (pelicula)


# _______
class Catalogo:

    listaProductos = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, productoInicial):
        self.listaProductos.append(productoInicial)

    def agregar(self, producto):  # p será un objeto Pelicula
        self.listaProductos.append(producto)

    def mostrar(self):
        for p in self.listaProductos:
            print(p)  # Print toma por defecto str(p)

producto=Productos("Radio",'S/. 300','Accesorios')
producto2=Productos("Llanta",'S/. 250','Accesorios')


c1=Catalogo(productoInicial)
c1.agregar(producto)
c1.agregar(producto2)
print("Se va mostrar la lista")
# c1.mostrar()

def listarCatalogo():
    return c1.mostrar()