from sanic import Sanic, response
from sanic.request import Request
from adapter import request_adapter

app = Sanic("MeuApp")

@app.post("/usuario/<user>")
async def receber_mensagem(request: Request, user: str):
    http_request = await request_adapter(request, user)

    # Regra de negocio
    # controller.use_case(http_request)

    return response.json({'resposta': 'Ola Mundo'})

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",  # acessível externamente
        port=5000,
        debug=True,     # mostra traceback em tempo real
        auto_reload=True  # recarrega código ao salvar
    )
