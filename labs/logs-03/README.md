# Filtrando e agregando logs

Filtre e agregue seus dados de log para encontrar informações específicas, obter insights e monitorar seus sistemas de forma mais eficiente. 

Você pode filtrar e agregar com base em campos estruturados, como carimbos de data/hora, níveis de log e endereços IP que você extraiu dos seus dados de log.

#### Antes de começar
Você precisa de alguns pré requisitos, para fazer esse laboratório, vamos lá.

Primeiro ponto crie um ingest pipeline

```
PUT _ingest/pipeline/logs-example-default
{
  "description": "Extracts the timestamp log level and host ip",
  "processors": [
    {
      "dissect": {
        "field": "message",
        "pattern": "%{@timestamp} %{log.level} %{host.ip} %{message}"
      }
    }
  ]
}
```

Depois disso crie um template

```
PUT _index_template/logs-example-default-template
{
  "index_patterns": [ "logs-example-*" ],
  "data_stream": { },
  "priority": 500,
  "template": {
    "settings": {
      "index.default_pipeline":"logs-example-default"
    }
  },
  "composed_of": [
    "logs-mappings",
    "logs-settings",
    "logs@custom",
    "ecs@dynamic_templates"
  ],
  "ignore_missing_component_templates": ["logs@custom"]
}
```

#### Filtrando os logs
Filtre seus dados usando os campos que você extraiu para que possa focar em dados de log com níveis de log específicos, intervalos de timestamp ou IPs de host. Você pode filtrar seus dados de log de diferentes maneiras:

- **Filtrar logs no Log Explorer** – Filtre e visualize dados de log no Kibana usando o Log Explorer.
- **Filtrar logs com Query DSL** – Filtre dados de log a partir das Ferramentas de Desenvolvimento usando Query DSL.

#### Filtrando logs no Log Explorer
O Log Explorer é uma ferramenta do Kibana que fornece automaticamente visualizações dos seus dados de log com base em integrações e fluxos de dados.

Você pode encontrar o Log Explorer no menu de Observabilidade, sob a opção Logs.

A partir do Log Explorer, você pode usar a Linguagem de Consulta do Kibana (KQL) na barra de pesquisa para refinar os dados de log exibidos no Log Explorer.

Por exemplo, você pode querer investigar um evento que ocorreu dentro de um intervalo de tempo específico.

Adicione alguns logs com diferentes carimbos de data/hora e níveis de log ao seu fluxo de dados:

- Vá até o menu devtools
- No console execute o comando

```
POST logs-example-default/_bulk
{ "create": {} }
{ "message": "2023-09-15T08:15:20.234Z WARN 192.168.1.101 Disk usage exceeds 90%." }
{ "create": {} }
{ "message": "2023-09-14T10:30:45.789Z ERROR 192.168.1.102 Critical system failure detected." }
{ "create": {} }
{ "message": "2023-09-10T14:20:45.789Z ERROR 192.168.1.105 Database connection lost." }
{ "create": {} }
{ "message": "2023-09-20T09:40:32.345Z INFO 192.168.1.106 User logout initiated." }
```

Para este exemplo, vamos procurar por logs com nível de log WARN ou ERROR que ocorreram em 14 ou 15 de setembro. A partir do Log Explorer:

- Insira a seguinte consulta KQL na barra de pesquisa para filtrar os logs com níveis de log de WARN ou ERROR:
```
log.level: ("ERROR" or "WARN")
```
- Clique no intervalo de tempo atual, selecione "Absolute" e defina a data de início para 14 de Setembro de 2023 @ 00:00:00.000.

![Calendário Kibana](https://www.elastic.co/guide/en/observability/current/images/logs-start-date.png)