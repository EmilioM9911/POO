from abc import ABC, abstractmethod
@abstractmethod
class Persona(ABC):

    def comogritan(self):
        pass

class Ñero(Persona):
    def comogritan(self):
        return "Y como gritan los ñeros: guau guau"

class Ñera(Persona):
    def comogritan(self):
        return "Y como gritan las ñeras: dale joto, dale joto"


nero = Ñero()
nero.comogritan()
nera=Ñera()
nera.comogritan()