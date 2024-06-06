class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"Grado: {self.grado}")


estudiante = Estudiante(nombre="Juan", edad=15, grado="Noveno")

estudiante.imprimir_informacion()

print(isinstance(estudiante, Persona))
print(isinstance(estudiante, Estudiante))

print(issubclass(Estudiante, Persona))