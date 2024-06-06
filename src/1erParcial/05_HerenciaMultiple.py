class Persona:
    def __init__(self, nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hablando {}".format(self.nombre))

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrarHabilidad(self):
        print("Mi habilidad es{}".format(self.habilidad))

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre,edad,nacionalidad,habilidad,salario,empresa,puesto):
        Persona.__init__(self, nombre,edad,nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        self.puesto = puesto

    def presentarse(self):
        print( f'Mi habilidad es {self.habilidad}')

roberto = EmpleadoArtista('Roberto','45','Mexicano','Cantar','100k','Google','Programador')
#print(roberto.presentarse()) #() Significa que se manda a llamar un método
roberto.presentarse()

roberto1 = EmpleadoArtista(nombre='emilio',)

herencia = isinstance(roberto,EmpleadoArtista)
#print(herencia)

herencia = issubclass(EmpleadoArtista,Artista)
print(herencia)