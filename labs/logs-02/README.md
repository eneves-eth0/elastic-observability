# Analisar e organizar logs

Se os seus dados de log são não estruturados ou semi-estruturados, você pode analisá-los e dividi-los em campos significativos.

Esses campos podem ser usados para explorar e analisar seus dados. Por exemplo, você pode encontrar logs dentro de um intervalo de tempo específico ou filtrar logs por nível de log para focar em possíveis problemas.

Após a análise, você pode usar os campos estruturados para organizar ainda mais seus logs, configurando um processador de redirecionamento para enviar logs específicos para diferentes datastreams.

## Extraindo campos estruturados

Torne seus logs mais úteis extraindo campos estruturados dos seus dados de log não estruturados. A extração de campos estruturados facilita a busca, análise e filtragem dos seus dados de log.

Siga os passos abaixo para ver como os seguintes dados de log não estruturados são indexados por padrão

```
2023-08-08T13:45:12.123Z WARN 192.168.1.101 Disk usage exceeds 90%.
```

Comece armazenando o documento no datastream logs-example-default:

- No Kibana, vá até **Managment** → **Dev Tools**.
- Na aba Console, adicione o log de exemplo ao Elasticsearch usando o seguinte comando:

```
POST logs-example-default/_doc
{
  "message": "2023-08-08T13:45:12.123Z WARN 192.168.1.101 Disk usage exceeds 90%."
}
```
- Agora veja o documento

```
GET /logs-example-default/_search
```

Você deve ter uma saída tipo essa:

```
{
  ...
  "hits": {
    ...
    "hits": [
      {
        "_index": ".ds-logs-example-default-2023.08.09-000001",
        ...
        "_source": {
          "message": "2023-08-08T13:45:12.123Z WARN 192.168.1.101 Disk usage exceeds 90%.",
          "@timestamp": "2023-08-09T17:19:27.73312243Z"
        }
      }
    ]
  }
}
```
O Elasticsearch indexa o campo de mensagem por padrão e adiciona um campo @timestamp. 

Como não foi definido um timestamp, ele é configurado para o momento atual.

Neste ponto, você pode procurar por frases no campo de mensagem, como WARN ou Disk usage exceeds. 

Por exemplo, use o seguinte comando para procurar pela frase WARN no campo de mensagem do log:
```
GET logs-example-default/_search
{
  "query": {
    "match": {
      "message": {
        "query": "WARN"
      }
    }
  }
}
```
Embora você possa procurar por frases no campo de mensagem, não é possível usar este campo para filtrar os dados de log.

No entanto, sua mensagem contém todos os seguintes campos potenciais que você pode extrair e usar para filtrar e agregar seus dados de log:

- **@timestamp** – `2023-08-08T13:45:12.123Z` – Extrair este campo permite que você organize os logs por data e hora. Isso é útil quando você quer visualizar seus logs na ordem em que ocorreram ou identificar quando problemas aconteceram.
- **log.level** – `WARN` – Extrair este campo permite que você filtre logs por severidade. Isso é útil se você quiser focar em logs de alta severidade, como WARN ou ERROR, e reduzir ruídos filtrando logs de baixa severidade, como os de nível INFO.
- **host.ip** – `192.168.1.101` – Extrair este campo permite que você filtre logs pelos endereços IP do host. Isso é útil se você quiser focar em hosts específicos com os quais está tendo problemas ou se quiser encontrar disparidades entre hosts.
- **message** – `Disk usage exceeds 90%`. – Você pode procurar por frases ou palavras no campo de mensagem.

### Extraindo o @timestamp

Quando você adicionou o log ao Elasticsearch na seção anterior, o campo @timestamp mostrou quando o log foi adicionado. O carimbo de data/hora que indica quando o log realmente ocorreu estava no campo de mensagem não estruturado:

```
"_source": {
    "message": "2023-08-08T13:45:12.123Z WARN 192.168.1.101 Disk usage exceeds 90%.",
    "@timestamp": "2023-08-09T17:19:27.73312243Z"
}
```

Ao investigar problemas, você deseja filtrar os logs pelo momento em que o problema ocorreu, não quando o log foi adicionado ao seu projeto. Para fazer isso, extraia o carimbo de data/hora do campo de mensagem não estruturado para o campo estruturado @timestamp, seguindo os seguintes passos:

- Use um ingest pipeline para extrair o @timestamp
- Teste o pipeline com o api simulate
- Configure o datastrem com um index template
- Crie o datastream

#### Usando o ingest pipeline para extrair o @timestamp

Pipelines de ingestão consistem em uma série de processadores que realizam transformações comuns em documentos recebidos antes de serem indexados.

Para extrair o campo @timestamp do log de exemplo, use um pipeline de ingestão com um processador dissect.

O processador dissect extrai campos estruturados de mensagens de log não estruturadas com base em um padrão que você define.

O Elasticsearch pode analisar carimbos de data/hora em string que estão nos formatos yyyy-MM-dd'T'HH:mm:ss.SSSZ e yyyy-MM-dd para campos de data.

Como o carimbo de data/hora do exemplo de log está em um desses formatos, você não precisa de processadores adicionais.

Carimbos de data/hora mais complexos ou não padronizados requerem um processador de data para analisar o carimbo de data/hora em um campo de data.

Use o seguinte comando para extrair o carimbo de data/hora do campo de mensagem para o campo @timestamp:

```
PUT _ingest/pipeline/logs-example-default
{
  "description": "Extracts the timestamp",
  "processors": [
    {
      "dissect": {
        "field": "message",
        "pattern": "%{@timestamp} %{message}"
      }
    }
  ]
}
```

#### Faça o teste do seu pipeline

A API de simulação de pipeline executa o pipeline de ingestão sem armazenar quaisquer documentos.

Isso permite que você verifique se o seu pipeline está funcionando usando múltiplos documentos. Execute o seguinte comando para testar o seu pipeline de ingestão com a API de simulação de pipeline

```
POST _ingest/pipeline/logs-example-default/_simulate
{
  "docs": [
    {
      "_source": {
        "message": "2023-08-08T13:45:12.123Z WARN 192.168.1.101 Disk usage exceeds 90%."
      }
    }
  ]
}
```

Seu resultado deve ser algo parecido com isso

```
{
  "docs": [
    {
      "doc": {
        "_index": "_index",
        "_id": "_id",
        "_version": "-3",
        "_source": {
          "message": "WARN 192.168.1.101 Disk usage exceeds 90%.",
          "@timestamp": "2023-08-08T13:45:12.123Z"
        },
        ...
      }
    }
  ]
}
```

#### Configure um datastrem com um index template
Após criar o seu pipeline de ingestão, execute o seguinte comando para criar um template de dados para o seu datastream

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
O template de exemplo acima define os seguintes modelos de componentes:

- **logs-mappings** – mapeamentos gerais para fluxos de dados de log que incluem a desativação da detecção automática de datas a partir de campos de string e especificação de mapeamentos para campos ECS de data_stream.
- **logs-settings** – configurações gerais para fluxos de dados de log, incluindo o seguinte:

  - A política de ciclo de vida padrão que realiza a rolagem quando o shard primário atinge 50 GB ou após 30 dias.
  - O pipeline padrão usa o carimbo de data/hora de ingestão se não houver um @timestamp especificado e coloca um gancho para o pipeline logs@custom. Se um pipeline logs@custom estiver instalado, ele é aplicado aos logs ingeridos neste fluxo de dados.
  - Define a flag ignore_malformed como verdadeira. Ao ingerir um grande lote de dados de log, um único campo malformado, como um endereço IP, pode fazer com que todo o lote falhe. Quando definido como verdadeiro, campos malformados com um tipo de mapeamento que suporta esta flag ainda são processados.
- **logs@custom** – um modelo de componente predefinido que não é instalado por padrão. Use este nome para instalar um modelo de componente personalizado para substituir ou estender qualquer um dos mapeamentos ou configurações padrão.
- **ecs@dynamic_templates** – modelos dinâmicos que garantem automaticamente que os mapeamentos do seu fluxo de dados estejam em conformidade com o Elastic Common Schema (ECS)."

#### Criando um datastream
Crie seu datastream usando o data stream naming scheme.

Nomeie seu data stream para corresponder ao nome do seu pipeline de ingestão, que neste caso é logs-example-default.

Publique o log de exemplo no seu data stream com este comando:

```
POST logs-example-default/_doc
{
  "message": "2023-08-08T13:45:12.123Z WARN 192.168.1.101 Disk usage exceeds 90%."
}
```
Veja seus docs usando o seguinte comando

```
GET /logs-example-default/_search
```

Você deve ter uma resposta parecida com essa

```
{
...
{
  ...
  "hits": {
    ...
    "hits": [
      {
        "_index": ".ds-logs-example-default-2023.08.09-000001",
        "_id": "RsWy3IkB8yCtA5VGOKLf",
        "_score": 1,
        "_source": {
          "message": "WARN 192.168.1.101 Disk usage exceeds 90%.",
          "@timestamp": "2023-08-08T13:45:12.123Z"
        }
      }
    ]
  }
}
```

> Desafio, extraia agora o log.level da sua mensagem de logs