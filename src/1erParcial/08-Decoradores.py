def decorador(funcion):

    def funcionDecorado():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de la función")
    return funcionDecorado
@decorador
def saludo():
    print('saludo')

saludo()

#sm = decorador(saludo)
#sm()