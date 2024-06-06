class Persona:
    def __init__(self, nombre,edad,):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, newNombre):
        self.__nombre = newNombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre

emilio = Persona(nombre='Emilio Márquez', edad=20)

#nombre = emilio.getNombre()
#print(nombre)

#emilio.setNombre("Emilio Márquez")
#print(emilio.getNombre())

nombre = emilio.nombre
print(nombre)

nombre = emilio.nombre
print(nombre)

del emilio.nombre