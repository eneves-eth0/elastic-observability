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

- Clique no final do intervalo de tempo atual, selecione "Absolute" e defina a data de término para 15 de Setembro de 2023 @ 23:59:59.999.

![Calendário Kibana](https://www.elastic.co/guide/en/observability/current/images/logs-end-date.png)

Na aba de documentos veja os resultados

![Calendário Kibana](https://www.elastic.co/guide/en/observability/current/images/logs-kql-filter.png)

#### Filtrando logs com query DSL
Query DSL é uma linguagem baseada em JSON que envia solicitações e recupera dados de índices e fluxos de dados.

Você pode filtrar seus dados de log usando Query DSL a partir das Ferramentas de Desenvolvedor.

Por exemplo, você pode querer solucionar um problema que aconteceu em uma data específica ou em um horário específico.

Para fazer isso, use uma consulta booleana com uma consulta de intervalo para filtrar pelo intervalo de timestamp específico e uma consulta de termo para filtrar pelos níveis de log WARN e ERROR.

Primeiro, a partir do Dev Tools, adicione alguns logs com diferentes timestamps e níveis de log ao seu data stream com o seguinte comando:

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

Vamos supor que você queira investigar um evento que ocorreu entre 14 e 15 de setembro. A seguinte consulta booleana filtra por logs com timestamps nesses dias que também tenham um nível de log de ERROR ou WARN.

```
POST /logs-example-default/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "2023-09-14T00:00:00",
              "lte": "2023-09-15T23:59:59"
            }
          }
        },
        {
          "terms": {
            "log.level": ["WARN", "ERROR"]
          }
        }
      ]
    }
  }
}
```

Você deve ter uma saida parecida com essa

```
{
  ...
  "hits": {
    ...
    "hits": [
      {
        "_index": ".ds-logs-example-default-2023.09.25-000001",
        "_id": "JkwPzooBTddK4OtTQToP",
        "_score": 0,
        "_source": {
          "message": "192.168.1.101 Disk usage exceeds 90%.",
          "log": {
            "level": "WARN"
          },
          "@timestamp": "2023-09-15T08:15:20.234Z"
        }
      },
      {
        "_index": ".ds-logs-example-default-2023.09.25-000001",
        "_id": "A5YSzooBMYFrNGNwH75O",
        "_score": 0,
        "_source": {
          "message": "192.168.1.102 Critical system failure detected.",
          "log": {
            "level": "ERROR"
          },
          "@timestamp": "2023-09-14T10:30:45.789Z"
        }
      }
    ]
  }
}
```
#### Agregando Logs
Utilize a agregação para analisar e resumir seus dados de log a fim de encontrar padrões e obter insights.

As agregações do tipo "bucket" organizam os dados de log em grupos significativos, facilitando a identificação de padrões, tendências e anomalias nos seus logs.

Por exemplo, você pode querer entender a distribuição de erros analisando a contagem de logs por nível de log.

Primeiro, a partir das Ferramentas de Desenvolvimento (Dev Tools), adicione alguns logs com diferentes níveis de log ao seu fluxo de dados usando o seguinte comando:

```
POST logs-example-default/_bulk
{ "create": {} }
{ "message": "2023-09-15T08:15:20.234Z WARN 192.168.1.101 Disk usage exceeds 90%." }
{ "create": {} }
{ "message": "2023-09-14T10:30:45.789Z ERROR 192.168.1.102 Critical system failure detected." }
{ "create": {} }
{ "message": "2023-09-15T12:45:55.123Z INFO 192.168.1.103 Application successfully started." }
{ "create": {} }
{ "message": "2023-09-14T15:20:10.789Z WARN 192.168.1.104 Network latency exceeding threshold." }
{ "create": {} }
{ "message": "2023-09-10T14:20:45.789Z ERROR 192.168.1.105 Database connection lost." }
{ "create": {} }
{ "message": "2023-09-20T09:40:32.345Z INFO 192.168.1.106 User logout initiated." }
{ "create": {} }
{ "message": "2023-09-21T15:20:55.678Z DEBUG 192.168.1.102 Database connection established." }
```

Agora rode o seguinte comando para agregar os logs por log.level

```
POST logs-example-default/_search?size=0&filter_path=aggregations
{
"size": 0,
"aggs": {
    "log_level_distribution": {
      "terms": {
        "field": "log.level"
      }
    }
  }
}
```

Você deve ter uma saída parecida com essa 

```
{
  "aggregations": {
    "error_distribution": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "ERROR",
          "doc_count": 2
        },
        {
          "key": "INFO",
          "doc_count": 2
        },
        {
          "key": "WARN",
          "doc_count": 2
        },
        {
          "key": "DEBUG",
          "doc_count": 1
        }
      ]
    }
  }
}
```

Você também pode combinar aggregations e queries.

Por exemplo, você pode querer limitar o escopo da aggregation anterior adicionando uma range query:

```
GET /logs-example-default/_search
{
  "size": 0,
  "query": {
    "range": {
      "@timestamp": {
        "gte": "2023-09-14T00:00:00",
        "lte": "2023-09-15T23:59:59"
      }
    }
  },
  "aggs": {
    "my-agg-name": {
      "terms": {
        "field": "log.level"
      }
    }
  }
}
```

Você deve ter um resultado parecido com esse

```
{
  ...
  "hits": {
    ...
    "hits": []
  },
  "aggregations": {
    "my-agg-name": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "WARN",
          "doc_count": 2
        },
        {
          "key": "ERROR",
          "doc_count": 1
        },
        {
          "key": "INFO",
          "doc_count": 1
        }
      ]
    }
  }
}
```