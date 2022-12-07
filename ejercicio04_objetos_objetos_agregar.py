class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        # print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} se estrenó ({})'.format(self.titulo, self.lanzamiento)

pelicula= Pelicula('Godzilla', '1:50 hrs', '27 de Octubre del 2000')
# print (pelicula)


# _______
class Catalogo:

    listaPeliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, pelicula):
        self.listaPeliculas.append(pelicula)

    def agregar(self, p):  # p será un objeto Pelicula
        self.listaPeliculas.append(p)

    def mostrar(self):
        for p in self.listaPeliculas:
            print(p)  # Print toma por defecto str(p)

p=Pelicula("wakanda",2,2022)
p1=Pelicula("wakanda 2",2,2023)
p2=Pelicula("Avengers",3,2019)

c1=Catalogo(p)
c1.agregar(p1)
c1.agregar(p2)
print("se va mostrar la lista")
c1.mostrar()