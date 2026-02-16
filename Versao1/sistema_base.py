from abc import ABC, abstractmethod

class sistemaRPG(ABC):
    @property
    @abstractmethod
    def nome(self):
        pass

    @property
    @abstractmethod
    def atributos(self):
        pass

    @abstractmethod
    def atributos_padrao(self):
        pass

    @abstractmethod
    def validar_atributos(self, atributos: dict[str, int]):
        pass

    @abstractmethod
    def listar_atributos(self, atributos: dict[str, int]):
        pass