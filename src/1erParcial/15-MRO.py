class Animal:
    def comer(self):
        print('El animal está comiendo')


class Mamifero(Animal):
    def amamantar(self):
        print('El animal está amamantando')


class Ave(Animal):
    def volar(self):
        print('El animal está volando')


class Murcielago(Mamifero, Ave):
    def murcielaguear(self):
        print('El murciélago está murcielagueando')


# Crear una instancia de Murcielago
murci = Murcielago()

# Llamar a los métodos de la instancia
murci.comer()
murci.amamantar()
murci.volar()
murci.murcielaguear()
print(Murcielago.mro())