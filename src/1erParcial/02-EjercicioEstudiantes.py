#Ejercicio 1-Crear clase de estudiante y mostrar mensaje
class Estudiante:
    def __init__(self, nombre, edad, carrera, cuatrimestre):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.cuatrimestre = cuatrimestre

    def estudiar(self):
        if self.carrera == 'sistemas':
            print(f'El estudiante {self.nombre} tiene {self.edad} años, estudia {self.carrera}, cursa el {self.cuatrimestre} cuatrimestre y está programando')
        elif self.carrera == 'negocios':
            print(f'El estudiante {self.nombre} tiene {self.edad} años, estudia {self.carrera}, cursa el {self.cuatrimestre} cuatrimestre y no hace nada')
        elif self.carrera == 'mecatronica':
            print(f'El estudiante {self.nombre} tiene {self.edad} años, estudia {self.carrera}, cursa el {self.cuatrimestre} cuatrimestre y está soldando')
        else:
            print(f'El estudiante {self.nombre} tiene {self.edad} años, estudia {self.carrera}, cursa el {self.cuatrimestre} cuatrimestre y está estudiando')


#.strip() elimina los espacios en blanco alrededor de la cadena ingresada
#.lower() convierte la cadena a minusculas, lo que permite que el programa funcione
#de manera correcta, independientemente del uso de mayusculas o minusculas.

carrera = input('Ingrese la carrera que desea estudiar: ').strip().lower()
nombre = input('Ingrese el nombre del estudiante: ').strip()
edad = input('Ingrese la edad del estudiante: ').strip()
cuatrimestre = input('Ingrese el cuatrimestre: ').strip()

estudiante1 = Estudiante(nombre, edad, carrera, cuatrimestre)
estudiante1.estudiar()
