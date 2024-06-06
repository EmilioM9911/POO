class ComidaMexicana:
    def __init__(self, tortilla, salsa, frijoles, queso, proteina):
        self.tortilla = tortilla
        self.salsa = salsa
        self.frijoles = frijoles
        self.queso = queso
        self.proteina = proteina

class Tacos(ComidaMexicana):
    def __init__(self, tortilla, salsa, frijoles, queso, proteina, cebolla, cilantro):
        super().__init__(tortilla, salsa, frijoles, queso, proteina)
        self.cebolla = cebolla
        self.cilantro = cilantro

    def cocinar(self):
        print(f"Los Tacos se preparan con {self.tortilla}, con {self.proteina} o algún otro tipo de carne, y lleva complementos como {self.cebolla}, {self.cilantro}, y algún tipo de {self.salsa} y puede llevar {self.frijoles} y {self.queso}")

class Chilaquiles(ComidaMexicana):
    def __init__(self, tortilla, salsa, frijoles, queso, proteina, cebolla, crema):
        super().__init__(tortilla, salsa, frijoles, queso, proteina)
        self.cebolla = cebolla
        self.crema = crema

    def cocinar(self):
        print(f"Los Chilaquiles se preparan con {self.tortilla} fritas, con {self.salsa}, con {self.crema} y con {self.cebolla}, puede llevar como complementos {self.proteina}, o algún otro tipo de proteína, {self.frijoles}")

class EnchiladasVerdes(ComidaMexicana):
    def __init__(self, tortilla, salsa, frijoles, queso, proteina, cebolla, aguacate):
        super().__init__(tortilla, salsa, frijoles, queso, proteina)
        self.cebolla = cebolla
        self.aguacate = aguacate

    def cocinar(self):
        print(f"Las Enchiladas Verdes se preparan con {self.tortilla} rellenas de {self.proteina}, cubiertas con {self.salsa} y adornadas con {self.cebolla} y {self.aguacate}. Pueden llevar {self.frijoles} y {self.queso}.")

class Sopes(ComidaMexicana):
    def __init__(self, tortilla, salsa, frijoles, queso, proteina, cebolla, crema):
        super().__init__(tortilla, salsa, frijoles, queso, proteina)
        self.cebolla = cebolla
        self.crema = crema

    def cocinar(self):
        print(f"Los Sopes se preparan con una base de masa de maíz, se rellenan con {self.proteina} y se adornan con {self.salsa}, {self.cebolla} y {self.crema}. Opcionalmente se pueden añadir {self.frijoles} y {self.queso}.")

# Instancias y uso
Taco1 = Tacos('Tortilla de maíz', 'roja', 'Frijoles', 'Queso', 'Carne', 'cebolla picada', 'cilantro')
Taco1.cocinar()

Chilaquiles1 = Chilaquiles('Tortilla de maíz', 'verde', 'frijoles', 'queso', 'pollo', 'cebolla morada', 'crema')
Chilaquiles1.cocinar()

Enchiladas1 = EnchiladasVerdes('Tortilla de maíz', 'verde', 'frijoles', 'queso', 'pollo', 'cebolla', 'aguacate')
Enchiladas1.cocinar()

Sopes1 = Sopes('Masa de maíz', 'roja', 'frijoles', 'queso', 'chorizo', 'cebolla', 'crema')
Sopes1.cocinar()
