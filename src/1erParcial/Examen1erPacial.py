from abc import ABC, abstractmethod

class Menu():
    def __init__(self, opcion):
        self.opcion = opcion

    def Opciones(self):
        if self.opcion =='1':
            @abstractmethod
            class SuperHeroe:
                def __init__(self, nombre, edad, superPoder):
                    self.nombre = nombre
                    self.edad = edad
                    self.superPoder = superPoder

                def MostrarSuperPoder(self):
                    pass

            class SuperPoder(SuperHeroe):
                def MostrarSuperPoder(self):
                    print(f'Mi SuperPoder es {self.superPoder}')

            Nombre = input('Ingrese el nombre del hero: ')
            Edad = input('Ingrese el edad: ')
            superpoder = input('Ingrese el superPoder: ')
            Heroe1 = SuperPoder(Nombre,Edad,superpoder)
            Heroe1.MostrarSuperPoder()

        elif self.opcion =='2':
            class Persona:
                def __init__(self, nombre, edad, actividad):
                    self.nombre = nombre
                    self.edad = edad
                    self.actividas = actividad

                def mostrarActividad(self):
                    print(f'Mi Actividad es: {self.actividas}')

                def Presentarse(self):
                    print(f'Mi Nombre es {self.nombre} y tengo {self.edad}.')

            NombreP = input('Ingrese el nombre de la persona: ')
            EdadP = input('Ingrese el edad: ')
            ActividadP = input('Ingrese la actividad: ')
            Persona1 = Persona(NombreP,EdadP,ActividadP)
            Persona1.mostrarActividad()
            Persona1.Presentarse()

        elif self.opcion =='3':
            class PersonaHeroe(SuperHeroe, Persona):
                def __init__(self, nombre, edad, SuperPoder, actividad):
                    SuperHeroe.__init__(self, nombre, edad, SuperPoder)
                    Persona.__init__(self, nombre, edad, actividad)

                def presentarse(self):
                    print(
                        f'Mi Nombre es {self.nombre}, tengo {self.edad}, mi SuperPoder es {self.superPoder} y mi actividad es {self.actividas}')

            PersonaHeroe = PersonaHeroe('Emilio', '20', 'Volar', actividad='Estudiar')
            PersonaHeroe.presentarse()
        elif self.opcion =='4':
            print('Saliendo del programa')


opcion = input('Ingresa una opcion del 1 al 4: ')
Menu1 = Menu(opcion)
Menu1.Opciones()