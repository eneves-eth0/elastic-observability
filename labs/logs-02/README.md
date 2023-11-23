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
