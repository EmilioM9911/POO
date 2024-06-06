class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar (self):
        print(f'Esta llamando {self.marca} {self.modelo} {self.camara}')

    def colgar (self):
        print(f'Esta colgando {self.marca} {self.modelo} {self.camara}')

celular1 = Celular('Apple', '15 pro max', '48mpx')
celular1.llamar()
celular1.colgar()

celular2 = Celular(
    'Samsung', 'S24', '68mpx')
celular2.llamar()


