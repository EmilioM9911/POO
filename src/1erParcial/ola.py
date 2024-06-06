class Calculadora:
    def __init__(self, valor_1, valor_2):
        self.valor_1 = valor_1
        self.valor_2 = valor_2

    def suma(self):
        print (self.valor_1 + self.valor_2)



mi_calculadora = Calculadora(10, 5)
mi_calculadora.suma()


