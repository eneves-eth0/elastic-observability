from flask import Flask, jsonify, request
import requests
import random
import logging
import ecs_logging
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

#configure logging settings
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# Add an ECS formatter to the Handler
handler = logging.StreamHandler()
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

app.config['ELASTIC_APM'] = {
  # Set the required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': 'service1',

  # Use if APM Server requires a secret token
  'SECRET_TOKEN': '<token>',

  # Set the custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': '<url>',

  # Set the service environment
  'ENVIRONMENT': 'prod',
  'LOG_ECS_REFORMATTING': 'override',
}

apm = ElasticAPM(app)

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    # Recebe o cadastro com nome e e-mail
    cadastro = request.get_json()
    nome = cadastro['nome']
    email = cadastro['email']
    logger.info("Usuario cadastrado com sucesso", extra={"http.request.method": "post"})

    numero_aleatorio = requests.get('http://service2:5001/numero_aleatorio').json()['numero_aleatorio']

    resposta = {'numero_aleatorio': numero_aleatorio}
    return jsonify(resposta)

@app.route('/erro400', methods=['GET'])
def erro400():
    logger.error("Falha ao chamar o endpoint", extra={"http.request.method": "post"})
    requests.get('http://service2:5001/erro400')
    return "Erro 400", 400

@app.route('/erro500', methods=['GET'])
def erro500():
    requests.get('http://service2:5001/erro500')

@app.route('/previsao_tempo')
def previsao_tempo():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo&appid={sua_chave_api}&units=metric&lang=pt_br'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        mensagem = 'Previsão do tempo para hoje em São Paulo: Temperatura de {}°C, {}'.format(temperatura, descricao)
        return jsonify({'mensagem': mensagem})
    else:
        logging.error("Deu ruim d+, corre")
        return jsonify({'erro': 'Erro ao obter previsão do tempo.'}), 500

if __name__ == '__main__':
    logger.info('Iniciando a aplicação')
    app.run(host='0.0.0.0', port=5002)
