from pagamento_interface import ServicoPagamentoInterface

class PagamentoPaypal(ServicoPagamentoInterface):
    def __init__(self, http):
        self.http_request = http

    def pagar(self, valor: float):
        self.http_request.post(valor)
        print("pagamento realizado")

class PagamentoDinheiro(ServicoPagamentoInterface):
    def pagar(self, valor: float):
        pass
