from abc import ABC, abstractmethod

class ServicoPagamentoInterface(ABC): # Não pode instanciar um objeto

    @abstractmethod
    def pagar(self, valor: float): # tenho obg que implementar no filho
        pass
