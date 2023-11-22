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