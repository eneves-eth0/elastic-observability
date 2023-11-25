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