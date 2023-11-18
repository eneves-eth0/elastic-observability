from flask import Flask, jsonify, request
import requests
import random
import logging
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

#configure logging settings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

app.config['ELASTIC_APM'] = {
  # Set the required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': '<nome_do_servico>',

  # Use if APM Server requires a secret token
  'SECRET_TOKEN': '<TOKEN>',

  # Set the custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': '<URL_APM_SEVER>',

  # Set the service environment
  'ENVIRONMENT': '<env>',
}

apm = ElasticAPM(app)

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    # Recebe o cadastro com nome e e-mail
    cadastro = request.get_json()
    nome = cadastro['nome']
    email = cadastro['email']

    # Chama o segundo microsserviço para gerar um número aleatório
    logging.info('Chamando o segundo microsserviço para gerar meu numero aleatorio')
    numero_aleatorio = requests.get('http://service2:5001/numero_aleatorio').json()['numero_aleatorio']

    # Retorna o número aleatório para o usuário
    logging.info('Retorna o numero aleatorio para o usuario')
    resposta = {'numero_aleatorio': numero_aleatorio}
    return jsonify(resposta)

@app.route('/erro400', methods=['GET'])
def erro400():
    logging.error('Deu ruim 400')
    requests.get('http://service2:5001/erro400')
    return "Erro 400", 400

@app.route('/erro500', methods=['GET'])
def erro500():
    logging.error('Deu ruim 500')
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
    logging.info('Iniciando a aplicação')
    app.run(host='0.0.0.0', port=5002)
