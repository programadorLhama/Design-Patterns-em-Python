from flask import Flask, request, jsonify
from adapter import request_adapter

app = Flask(__name__)

@app.route('/usuario/<user>', methods=['POST'])
def receber_mensagem(user):
    http_request = request_adapter(request)

    # Regra de negocio
    # controller.use_case(http_request)
    print(http_request)
    
    return jsonify({'resposta': 'Ola Mundo'}), 200

if __name__ == '__main__':
    app.run(debug=True)
