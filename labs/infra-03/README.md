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