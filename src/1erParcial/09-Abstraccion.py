class Auto:
    def __init__(self):
        self._estado = "Apagado"

    def encender(self):
        self._estado = "Encendido"
        print("El carro esta encendido")

    def comducir(self):
        if self._estado == "Apagado":
            self.encender()
        print("Conduciendo auto")

miAuto = Auto()
miAuto.comducir()