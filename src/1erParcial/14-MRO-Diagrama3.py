class AAA:
    def hablar(self):
        print('Clase AAA')
class BBB(AAA):
    def hablar(self):
        print('Clase BBB')
class CCC(AAA):
    def hablar(self):
        print('Clase CCC')
class DDD(BBB, CCC):
    def hablar(self):
        print('Clase DDD')
class EEE(BBB):
    def hablar(self):
        print('Clase EEE')
class FFF(CCC):
    def hablar(self):
        print('Clase FFF')
class O4(DDD, EEE, FFF):
    def hablar(self):
        print('Clase 04')

Objeto = O4()
print(O4.mro())