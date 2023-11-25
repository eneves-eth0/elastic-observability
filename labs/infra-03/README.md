# Analisando e comparando hosts
A página Hosts oferece uma visão baseada em métricas da sua infraestrutura, apoiada por uma interface fácil de usar chamada Lens. 

Na página Hosts, você pode visualizar métricas de saúde e desempenho para ajudá-lo a:

- Analisar e comparar hosts sem a necessidade de construir novos dashboards.
- Identificar quais hosts acionam mais alertas.
- Solucionar e resolver problemas rapidamente.
- Visualizar dados históricos para descartar falsos alertas e identificar causas raízes.
- Filtrar e pesquisar os dados para se concentrar nos hosts que mais lhe interessam.

Para acessar esta página a partir do menu principal do Kibana, vá para Observability → Infrastructure → Hosts.

![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts.png)

A página Hosts oferece várias maneiras de visualizar métricas de host:

- Os blocos de visão geral mostram o número de hosts retornados pela sua pesquisa, além das médias de métricas-chave, incluindo uso de CPU, uso de memória e throughput.
- O controle de limite de Hosts determina o número máximo de hosts mostrados na página. O padrão é 50, o que significa que a página mostra dados para os 50 hosts principais com base nos carimbos de data/hora mais recentes. Você pode aumentar o limite de hosts para ver dados de mais hosts, mas isso pode impactar o desempenho da consulta.
- A tabela de Hosts mostra uma divisão das métricas para cada host. Você pode precisar navegar pela lista ou alterar o número de linhas exibidas em cada página para ver todos os seus hosts.
- Cada nome de host é um link ativo para uma página de detalhes do host, que inclui métricas, metadados do host, alertas, processos, logs e anomalias. Você pode opcionalmente abrir os detalhes do host em uma sobreposição.
- As colunas da tabela são ordenáveis, mas note que o comportamento de ordenação é aplicado ao conjunto de dados já retornado.
- As abas na parte inferior da página mostram uma visão geral das métricas, logs e alertas para todos os hosts retornados pela sua pesquisa.

## Filtrando a visão de hosts

A página Hosts oferece vários mecanismos para filtrar os dados na página:

- Insira uma consulta de pesquisa para mostrar métricas que correspondam aos seus critérios de pesquisa. Por exemplo, para ver métricas de hosts executando em Linux, digite host.os.type : "linux". Caso contrário, você verá métricas para todos os seus hosts monitorados (até o número de hosts especificado pelo limite de hosts).
- Selecione critérios adicionais para filtrar a visualização:

  - Na lista Sistema Operacional, selecione um ou mais sistemas operacionais e inclua (ou exclua) métricas para esses hosts.
  - Na lista Provedor de Nuvem, selecione um ou mais provedores de nuvem para incluir (ou excluir) métricas dos provedores de nuvem selecionados.
- Altere o intervalo de datas no filtro de tempo, ou clique e arraste em uma visualização para alterar o intervalo de datas.
- Dentro de uma visualização, clique em um ponto em uma linha e aplique filtros para definir outras visualizações na página para o mesmo tempo e/ou host.

## Visualiando métricas
Na aba Metrics, visualize as tendências das métricas ao longo do tempo, incluindo carga normalizada, uso de CPU, uso de memória, rede inbound, rede outbound, leituras de IOPS do disco e escritas de IOPS do disco.

Posicione o cursor sobre uma linha para visualizar as métricas em um ponto específico no tempo. Dentro de cada visualização, você pode escolher inspecionar e baixar as métricas ou abrir a visualização no Lens.

## Inspecionando e fazendo download das métricas
Você pode acessar uma visualização baseada em texto dos dados subjacentes às suas visualizações de métricas e, opcionalmente, baixar os dados para um arquivo separado por vírgulas (CSV).

Passe o cursor sobre uma visualização e, em seguida, no canto superior direito, clique no ícone de reticências para inspecionar os dados.
![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts-inspect.png)

No painel lateral, clique em Download CSV para baixar dados formatados ou brutos em um arquivo CSV.

Observe que você pode alterar a visualização para View: Requests para explorar a solicitação usada para buscar os dados e a resposta retornada do Elasticsearch. Você pode clicar em links para inspecionar e analisar mais a fundo a solicitação no Dev Console ou no Search Profiler.

## Abrindo no lens

As visualizações de métricas são impulsionadas pelo Lens, o que significa que você pode continuar sua análise no Lens se precisar de mais flexibilidade. Passe o cursor sobre uma visualização e, em seguida, clique no ícone de reticências no canto superior direito para abrir a visualização no Lens.

![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts-open-in-lens.png)

No Lens, você pode examinar todos os campos e fórmulas usados para criar a visualização, fazer modificações na visualização e salvar suas alterações.

## Visualizando Logs
Na aba Logs, visualize logs dos sistemas que você está monitorando e procure por entradas de log específicas. Esta visualização mostra logs de todos os hosts retornados pela consulta atual.

![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts-logs.png)

## Visualizando Alertas
Na aba Alerts, visualize alertas ativos para identificar problemas. Use esta visualização para descobrir quais hosts acionaram alertas e identificar as causas raízes. Esta visualização mostra alertas de todos os hosts retornados pela consulta atual.

No menu Ações, você pode escolher:

- Adicionar o alerta a um caso novo ou existente.
- Visualizar detalhes da regra.
- Visualizar detalhes do alerta.

![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts-view-alerts.png)

## Por que eu vejo linhas pontilhadas no meu gráfico?
Existem algumas razões pelas quais você pode ver linhas tracejadas nos seus gráficos.

- O intervalo do gráfico é muito curto
- Faltam dados
- O intervalo do gráfico é muito curto e faltam dados

### O intervalo do gráfico é muito curto
Neste exemplo, a taxa de emissão de dados é menor do que o intervalo do gráfico do Lens. Uma linha tracejada conecta os pontos de dados conhecidos para facilitar a visualização das tendências nos dados.

![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts-dashed.png)

O intervalo do gráfico é definido automaticamente dependendo da duração do tempo selecionado. Para corrigir esse problema, altere o intervalo de tempo selecionado no topo da página.

### Faltam dados
Uma linha sólida indica que o intervalo do gráfico está ajustado adequadamente para a taxa de transmissão de dados. Neste exemplo, uma linha sólida se transforma em uma linha tracejada, indicando dados ausentes. Você pode querer investigar este período de tempo para determinar se há uma interrupção ou problema.

![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts-missing-data.png)

### O intervalo é muito curto e faltam dados

Na captura de tela abaixo, a taxa de emissão de dados é menor do que o intervalo do gráfico do Lens e há dados ausentes.

Esses dados ausentes podem ser difíceis de identificar à primeira vista. As caixas verdes delimitam as emissões regulares de dados, enquanto os dados ausentes são delimitados em rosa. Semelhante ao cenário acima, você pode querer investigar o período de tempo com os dados ausentes para determinar se há uma interrupção ou problema.

![Infra](https://www.elastic.co/guide/en/observability/current/images/hosts-dashed-and-missing.png)
