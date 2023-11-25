# Detectando anomalias em métricas
Quando os recursos de detecção de anomalias de aprendizado de máquina estão ativados, você pode criar trabalhos de machine learning para detectar e inspecionar anomalias no uso de memória e tráfego de rede para hosts e pods do Kubernetes.

Você pode modelar o uso de memória do sistema, juntamente com o tráfego de rede de entrada e saída em hosts ou pods. Você pode detectar aumentos incomuns no uso de memória e tráfego de rede de entrada ou saída anormalmente alto em hosts ou pods.

## Ative trabalhos de machine learning para hosts ou pods do Kubernetes

Crie um trabalho de machine learning para detectar automaticamente uso anormal de memória e tráfego de rede.

Uma vez que você cria trabalhos de machine learning, você não pode alterar as configurações. Você pode recriar esses trabalhos mais tarde. No entanto, você removerá quaisquer anomalias detectadas anteriormente.

- Vá para Observabilidade → Infraestrutura → Inventário e clique no link Detecção de Anomalias no topo da página.
- Você será solicitado a criar um trabalho de machine learning para Hosts ou Pods do Kubernetes. Clique em Ativar.
- Escolha uma data de início para a análise de machine learning.

Os trabalhos de machine learning analisam as últimas quatro semanas de dados e continuam a funcionar indefinidamente.

- Selecione um campo de partição.
As partições permitem que você crie modelos independentes para diferentes grupos de dados que compartilham comportamentos semelhantes. Por exemplo, você pode querer construir modelos separados para tipo de máquina ou zona de disponibilidade na nuvem, de modo que as anomalias não sejam ponderadas igualmente entre os grupos.

- Por padrão, os trabalhos de machine learning analisam todos os seus dados de métricas, e os resultados são listados na aba Anomalias. Você pode filtrar essa lista para visualizar apenas os trabalhos ou métricas que lhe interessam. Por exemplo, você pode filtrar por nome do trabalho e nome do nó para visualizar trabalhos específicos de detecção de anomalias para aquele host.
- Clique em Ativar trabalhos.
- Você está agora pronto para explorar suas anomalias de métricas. Clique em Anomalias.

![Infra](https://www.elastic.co/guide/en/observability/current/images/metrics-ml-jobs.png)

A tabela Anomalias exibe uma lista de cada trabalho de detecção de anomalias de métricas individuais para o host específico ou pod do Kubernetes. Por padrão, os trabalhos de anomalias são ordenados por tempo para mostrar o trabalho mais recente.

Junto com cada trabalho de anomalia e o nome do nó, são listadas anomalias detectadas com uma pontuação de severidade igual ou superior a 50. Essas pontuações representam uma severidade de "aviso" ou superior no período de tempo selecionado. O valor resumido representa o aumento entre o valor real e o valor esperado ("típico") da métrica no resultado do registro de anomalia.

Para aprofundar e analisar a anomalia da métrica, selecione Ações → Abrir no Anomaly Explorer para visualizar o Anomaly Explorer em Machine Learning. Você também pode selecionar Ações → Mostrar no Inventário para visualizar a página de Inventário do host ou pods do Kubernetes, filtrada pela métrica específica.

## Gráfico histórico

Na página de Inventário, clique em Mostrar histórico para visualizar os valores das métricas dentro do intervalo de tempo selecionado. Anomalias detectadas com uma pontuação de anomalia igual ou superior a 50 são destacadas em vermelho. Para examinar as anomalias detectadas, use o Anomaly Explorer.

![Infra](https://www.elastic.co/guide/en/observability/current/images/metrics-history-chart.png)

