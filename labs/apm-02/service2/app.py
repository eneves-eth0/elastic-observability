from flask import Flask, jsonify
import requests
import random
import ecs_logging
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
  # Set the required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': 'service2',

  # Use if APM Server requires a secret token
  'SECRET_TOKEN': '<token>',

  # Set the custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': '<url>',

  # Set the service environment
  'ENVIRONMENT': 'prod',
  'LOG_ECS_REFORMATTING': 'override',
}

apm = ElasticAPM(app)

@app.route('/numero_aleatorio', methods=['GET'])
def gerar_numero_aleatorio():
    # Gera um número aleatório entre 1 e 100
    numero_aleatorio = random.randint(1, 100)

    # Retorna o número aleatório em formato JSON
    resposta = {'numero_aleatorio': numero_aleatorio}
    return jsonify(resposta)
@app.route('/erro400', methods=['GET'])
def erro400():
    return "Erro 400", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
