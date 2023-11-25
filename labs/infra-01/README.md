# Visualizando métricas por tipo de recursos
A página Inventory oferece uma visão baseada em métricas de toda a sua infraestrutura, agrupada pelos recursos que você está monitorando. 

Todos os recursos monitorados que emitem um conjunto central de métricas de infraestrutura são exibidos para fornecer uma visão rápida da saúde geral da sua infraestrutura.

Para acessar esta página a partir do menu principal do Kibana, vá para Observability → Infrastructure → Inventory.

![Infra](https://www.elastic.co/guide/en/observability/current/images/metrics-app.png)

#### Filtrando a visão de inventário
Para começar sua análise, selecione o tipo de recursos que você deseja mostrar na visão de alto nível. 

No menu Show, selecione uma das seguintes opções:

- Hosts (o padrão)
- Kubernetes Pods
- Docker Containers
- AWS, que inclui instâncias EC2, buckets S3, bancos de dados RDS e filas SQS

Quando você passa o mouse sobre cada recurso no mapa de waffle, as métricas específicas para aquele recurso são exibidas.

Você pode ordenar por recurso, agrupar o recurso por campos específicos relacionados a ele e ordenar por nome ou valor da métrica. 

Por exemplo, você pode filtrar a visualização para exibir o uso de memória dos seus Kubernetes pods, agrupados por namespace e ordenados pelo valor de uso de memória.

![Infra](https://www.elastic.co/guide/en/observability/current/images/kubernetes-filter.png)

Você também pode usar a barra de pesquisa para criar consultas estruturadas usando a Kibana Query Language. Por exemplo, digite host.hostname : "host1" para visualizar apenas as informações do host1.

Para examinar as métricas de um momento específico, use o filtro de tempo para selecionar a data e a hora.

#### Visualizando hosts e métricas
Por padrão, a página Inventory exibe um mapa de waffle que mostra os hosts que você está monitorando e o uso atual da CPU para cada host. Alternativamente, você pode clicar no ícone de visualização em tabela para mudar para uma visualização em tabela.

Sem sair da página Inventory, você pode visualizar métricas aprimoradas relacionadas a cada host em execução na sua infraestrutura. No mapa de waffle, selecione um host para exibir a sobreposição de detalhes do host.

O detalhamento de hosts tem as seguintes abas:

## Visão geral
![Infra](https://www.elastic.co/guide/en/observability/current/images/metrics-overlay.png)

## Metadata
![Infra](https://www.elastic.co/guide/en/observability/current/images/metadata-overlay.png)

## Processos
![Infra](https://www.elastic.co/guide/en/observability/current/images/processes-overlay.png)

## Logs
![Infra](https://www.elastic.co/guide/en/observability/current/images/logs-overlay.png)

## Anomalias
![Infra](https://www.elastic.co/guide/en/observability/current/images/anomalies-overlay.png)

## Osquery
![Infra](https://www.elastic.co/guide/en/observability/current/images/osquery-overlay.png)


A aba Osquery permite que você construa declarações SQL para consultar os dados do seu host. 

Você pode criar e executar consultas ao vivo ou salvas contra o Elastic Agent. Os resultados do Osquery são armazenados no Elasticsearch, para que você possa usar o Elastic Stack para pesquisar, analisar e visualizar as métricas do seu host.

Para visualizar mais informações sobre a consulta, clique na aba Status. O status de uma consulta pode resultar em sucesso, erro (junto com uma mensagem de erro) ou pendente (se o Elastic Agent estiver offline).

Outras opções incluem:

- Ver em Discover para pesquisar, filtrar e visualizar informações sobre a estrutura dos campos de métricas do host. Para saber mais, consulte Discover.
- Ver em Lens para criar visualizações com base nos campos de métricas do seu host. Para saber mais, consulte Lens.
- Visualizar os resultados em modo de tela cheia.
- Adicionar, remover, reordenar e redimensionar colunas.
- Ordenar nomes de campos em ordem ascendente ou descendente.

## Ver métricas para outros recursos
Quando você tiver pesquisado e filtrado por um recurso específico, você pode aprofundar para analisar as métricas relacionadas a ele. 

Por exemplo, ao visualizar Kubernetes Pods na visão de alto nível, clique no Pod que deseja analisar e selecione Kubernetes Pod metrics para ver métricas detalhadas:

![Infra](https://www.elastic.co/guide/en/observability/current/images/pod-metrics.png)

