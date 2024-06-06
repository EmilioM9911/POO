class Z:
    def hablar(self):
        print('Clase Z')
class K1(Z):
    def hablar(self):
        print('Clase K1')
class K2(Z):
    def hablar(self):
        print('Clase K2')
class K3(Z):
    def hablar(self):
        print('Clase K3')
class CC(K1):
    def hablar(self):
        print('Clase CC')
class AA(K1, K3):
    def hablar(self):
        print('Clase AA')
class BB(K1, K2):
    def hablar(self):
        print('Clase BB')
class DD(K3, K2):
    def hablar(self):
        print('Clase DD')
class EE(K1):
    def hablar(self):
        print('Clase EE')
class O3(CC, AA, BB, DD, EE):
    def hablar(self):
        print('Clase O0O')
Objeto = O3()
print(O3.mro())
