from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    @abstractmethod
    def hacerActividad(self):
        pass
    def presentarse(self):
        print(f"Hola mi nommbre es: {self.nombre}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacerActividad(self):
        print(f"mi actividad es: {self.actividad}")


class Programador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    def hacerActividad(self):
        print(f"mi actividad es: {self.actividad}")


class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacerActividad(self):
        print(f"mi actividad es: {self.actividad}")

emilio = Estudiante('Emilio', 20, 'Male', 'Dormir')
emilio.presentarse()
emilio.hacerActividad()

emilio1 = Programador('Isaac', 21, 'Male', 'Programar')
emilio1.presentarse()
emilio1.hacerActividad()

emilio2 = Profesor('Andrés', 20, 'Male', 'Dar clase')
emilio2.presentarse()
emilio2.hacerActividad()

