# Enviando logs de qualquer fonte

Este lab  vai te  ensinar como enviar um arquivo de log para o Elasticsearch usando Elastic Agent Standalone. 

Você aprenderá a configurar o **Elastic Agent** e seus fluxos de dados utilizando o arquivo **elastic-agent.yml**, além de como consultar seus logs usando os fluxos de dados que você configurou.

## Pré-requisitos

Para seguir os passos deste guia, você precisa de uma implantação do Elastic Stack que inclua:

- Elasticsearch para armazenar e pesquisar dados.
- Kibana para visualizar e gerenciar dados.
- Usuário do Kibana com todos os privilégios em 'Fleet' e 'Integrações'. 
- Servidor de Integrações (incluído por padrão em cada implantação do Serviço Elasticsearch).

## Instalando e configurando o elastic agent

### Passo 1: Faça o download e extraia o arquivo de instalação

**macOS**
```
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.11.1-darwin-x86_64.tar.gz
tar xzvf elastic-agent-8.11.1-darwin-x86_64.tar.gz
```
**Linux**
```
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.11.1-linux-x86_64.tar.gz
tar xzvf elastic-agent-8.11.1-linux-x86_64.tar.gz
```
**Windows**
```
# PowerShell 5.0+
wget https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.11.1-windows-x86_64.zip -OutFile elastic-agent-8.11.1-windows-x86_64.zip
Expand-Archive .\elastic-agent-8.11.1-windows-x86_64.zip
```
### Passo2: Instale e inicie o agent
Após baixar e extrair o pacote de instalação, você estará pronto para instalar o **Elastic Agent**. A partir do diretório do **Elastic Agent**, execute o comando de instalação que corresponde ao seu sistema:

**macOS**
```
sudo ./elastic-agent install
```
**Linux**
```
sudo ./elastic-agent install
```
**Windows**
```
.\elastic-agent.exe install
```
Durante o processo de instalação vão ser feitas algumas perguntas:
- Quando você for perguntado se deseja instalar o agent responda: Y
- Quando você for perguntado se deseja se ligar a um servidor fleet responda: n

### Passo 3: Configure o Elastic Agent
Com o Elastic Agent instalado, configure-o atualizando o arquivo **elastic-agent.yml**.

#### Encontre seu arquivo de configuração
Após instalar o agente, você encontrará o arquivo **elastic-agent.yml** em um dos seguintes locais, de acordo com o seu sistema:

**macOS**
```
/Library/Elastic/Agent/elastic-agent.yml
```
**Linux**
```
/opt/Elastic/Agent/elastic-agent.yml
```
**Windows**
```
C:\Program Files\Elastic\Agent\elastic-agent.yml
```

#### Atualizando o arquivo de configuração
Segue um exemplo de configuração para um Elastic Agent independente. 
Para configurar o seu Elastic Agent, substitua o conteúdo do arquivo **elastic-agent.yml** por esta configuração:

```
outputs:
  default:
    type: elasticsearch
    hosts: '<endpoint-do-elasticsearch>:<porta>'
    api_key: 'sua-chave-api'
inputs:
  - id: seu-log-id
    type: filestream
    streams:
      - id: seu-log-stream-id
        data_stream.dataset: generic
        paths:
          - /var/log/seus-logs.log
```
Coloque os seguintes valores nos campos:
- **hosts:** Copieo endereço do seu elasticsearch para essa diretiva, se estiver usando elastic cloud a porta padrão é a 443

![Screenshot da tela do deployment da elastic cloud](https://www.elastic.co/guide/en/observability/current/images/es-endpoint-cluster-id.png)

- **api-key:** Use uma chave API para conceder ao agente acesso ao Elasticsearch. Para criar uma chave API para o seu agente, consulte a documentação 'Criar chaves API para agentes independentes'.
- **inputs.id:** Um identificador único para a sua entrada.
- **type:** O tipo de entrada. Para coletar logs, defina isso como filestream.
- **streams.id:** Um identificador único para o seu fluxo de dados de log.
- **data_stream.dataset:**  O nome para o seu fluxo de dados do conjunto de dados. Nomeie este fluxo de dados com algo que signifique a fonte dos dados. O valor padrão é genérico.
- **paths:** O caminho para os seus arquivos de log. Você também pode usar um padrão como /var/log/your-logs.log*.

#### Reinicie o Elastic Agent
Após atualizar o seu arquivo de configuração, você precisa reiniciar o Elastic Agent:

Primeiro, pare o Elastic Agent e seus executáveis relacionados usando o comando que funciona com o seu sistema:

**macOS**
```
sudo launchctl unload /Library/LaunchDaemons/co.elastic.elastic-agent.plist
```
**Linux**
```
sudo service elastic-agent stop
```
**Windows**
```
Stop-Service Elastic Agent
```

Depois reinicie o Elastic Agent:
**macOS**
```
sudo launchctl load /Library/LaunchDaemons/co.elastic.elastic-agent.plist
```
**Linux**
```
sudo service elastic-agent start
```
**Windows**
```
Start-Service Elastic Agent
```

Agora acesse o kibana e veja seus logs na aba de streams.