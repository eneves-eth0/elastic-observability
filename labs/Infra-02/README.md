# Explorando métricas de infraestrutura sobre o tempo

A página Metrics Explorer permite que você crie visualizações de séries temporais baseadas na agregação das suas métricas, compare-as com métricas relacionadas e as desmembre por campo de sua escolha. Você pode agrupar e criar visualizações de métricas para um ou mais recursos que está monitorando.

Além disso, para análises detalhadas das suas métricas, você pode anotar e salvar visualizações para seus dashboards personalizados usando o Time Series Visual Builder (TSVB) dentro do Kibana.

Para acessar esta página a partir do menu principal do Kibana, vá para Observability → Infrastructure e, em seguida, clique em Metrics Explorer.

![Infra](https://www.elastic.co/guide/en/observability/current/images/metrics-explorer.png)

Por padrão, a página Metrics Explorer exibe o uso da CPU para hosts, Kubernetes pods e Docker containers. A configuração inicial tem a agregação Average selecionada, o campo of é preenchido com as métricas padrão, e o dropdown graph per está configurado para Everything.

Como exemplo, vamos visualizar as métricas de carga do sistema para os hosts que estamos monitorando atualmente.

- No campo of, exclua as métricas selecionadas e, em seguida, adicione system.load.1, system.load.5 e system.load.15.

O gráfico exibe os valores médios das métricas que você selecionou.

- No dropdown graph per, adicione host.name.

Agora há um gráfico individual exibindo os valores médios das métricas para cada host.

![Infra](https://www.elastic.co/guide/en/observability/current/images/metrics-explorer-filter.png)

- Selecione Ações no canto superior direito de um dos gráficos e, em seguida, clique em Adicionar filtro.

Este gráfico agora exibe as métricas apenas para aquele host. O filtro adicionou um filtro da Kibana Query Language para host.name na segunda linha da configuração do Metrics Explorer.

- Vamos analisar algumas métricas específicas do host. No campo of, exclua cada uma das métricas de carga do sistema.

- Para explorar o tráfego de rede de saída, insira a métrica host.network.egress.bytes. Este é um valor que aumenta monotonicamente, então, no dropdown de agregação, selecione Rate.

- Os hosts possuem várias interfaces de rede, então é mais significativo exibir um gráfico para cada interface de rede. No dropdown graph per, adicione o campo system.network.name.

Agora há um gráfico separado para cada interface de rede.

- Vamos visualizar um dos gráficos no TSVB. Escolha um gráfico, clique em Ações e, em seguida, selecione Abrir em Visualize.

Nesta visualização, o máximo de host.network.egress.bytes é exibido, filtrado por host.name e system.network.name.

![Infra](https://www.elastic.co/guide/en/observability/current/images/metrics-time-series.png)