from pagamentos import PagamentoDinheiro, PagamentoPaypal
from http_request import HttpRequest

def pagamento_factory(tipo: str):
    if tipo == "dinheiro":
        return PagamentoDinheiro()
    if tipo == "online":
        obj_http = HttpRequest()
        return PagamentoPaypal(obj_http)


pagamento = pagamento_factory("online")
pagamento.pagar(444)
