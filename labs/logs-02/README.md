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