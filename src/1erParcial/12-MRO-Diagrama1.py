class A:
    def hablar(self):
        print('Clase A')

class B(A):
    def hablar(self):
        print('Clase B')

class C(B):
    def hablar(self):
        print('Clase C')

class D(A):
    def hablar(self):
        print('Clase D')

class E(C, D):
    def hablar(self):
        print('Clase E')

class F(D):
    def hablar(self):
        print('Clase F')

class G(E):
    def hablar(self):
        print('Clase G')

class H(E):
    def hablar(self):
        print('Clase H')

class O(F, G, H):
    def hablar(self):
        print('Clase O')

Objeto = O()
print(O.mro())




