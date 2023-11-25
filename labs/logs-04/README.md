# Monitoramento de Logs

### Tail logs
Dentro do aplicativo Logs, a página Stream permite que você monitore todos os eventos de log que chegam dos seus servidores, máquinas virtuais e contêineres em uma visualização centralizada. Você pode considerar isso como um tail -f no seu navegador, juntamente com o poder da pesquisa.

Clique em Stream Live para visualizar um fluxo contínuo de mensagens de log em tempo real, ou clique em Stop streaming para visualizar logs históricos de um intervalo de tempo especificado.

#### Filtrando Logs
Para ajudá-lo a começar sua análise mais rapidamente e extrair campos dos seus logs, use a barra de pesquisa para criar consultas estruturadas usando a Linguagem de Consulta Kibana.

Por exemplo, insira host.hostname : "host1" para ver apenas as informações do host1.

Além disso, clique em "Highlights" e insira um termo que você gostaria de localizar dentro dos eventos de log.

O histograma de Logs, localizado à direita, destaca o número de termos descobertos e quando o evento de log foi ingerido.

Isso ajuda você a pular rapidamente entre áreas potenciais de interesse em grandes quantidades de logs ou, em um nível mais alto, e visualizar quando um grande número de eventos ocorreu.

#### Inspecionando os eventos de logs
Quando você tiver pesquisado e filtrado seus logs para um evento de log específico, talvez queira examinar os metadados e os campos estruturados associados a esse evento.

Para visualizar os detalhes do documento do evento de Log no painel lateral, passe o mouse sobre o evento de log, clique em Ver ações para a linha e, em seguida, selecione Ver detalhes.

Para aprimorar ainda mais o fluxo de trabalho de monitoramento de logs, os ícones ao lado de cada valor de campo permitem que você filtre os logs por aquele valor

![Calendário Kibana](https://www.elastic.co/guide/en/observability/current/images/log-event-details.png)

#### Visualizando logs contextuais
Uma vez que seus logs estejam filtrados e você encontre uma linha de log interessante, o verdadeiro contexto que você procura é o que aconteceu antes e depois dessa linha de log dentro dessa fonte de dados.

Por exemplo, se você está executando aplicações containerizadas em um cluster Kubernetes, você filtra os logs pelo termo error e encontra uma linha de log de erro interessante.

O contexto que você deseja é o que aconteceu antes e depois da linha de erro dentro dos logs deste contêiner e aplicação.

Passe o mouse sobre o evento de log, clique em Ver ações para a linha e, em seguida, selecione Ver no contexto. O contexto é preservado e ajuda você a encontrar a causa raiz o mais rápido possível.

![Logs](https://www.elastic.co/guide/en/observability/current/images/contextual-logs.png)

#### Categorizando entradas de logs
Eventos de log de aplicação são frequentemente não estruturados e contêm dados variáveis.

Muitas mensagens de log são iguais ou muito semelhantes, então classificá-las pode reduzir milhões de linhas de log em apenas algumas categorias.

Dentro do aplicativo Logs, a página Categorias permite que você identifique rapidamente padrões nos seus eventos de log.

Em vez de identificar manualmente logs semelhantes, a visualização de categorização de logs lista eventos de log que foram agrupados com base em suas mensagens e formatos, para que você possa agir mais rapidamente.

#### Criando categorias de logs
Crie um job de machine learning para categorizar mensagens de log automaticamente.

O machine learning observa as partes estáticas da mensagem, agrupa mensagens semelhantes, classifica-as em categorias de mensagem e detecta contagens de mensagens anormalmente altas nas categorias.

![Logs](https://www.elastic.co/guide/en/observability/current/images/log-create-categorization-job.jpg)

- Selecione Categorias, e você será solicitado a usar machine learning para criar categorizações de taxa de log.
- Escolha um intervalo de tempo para a análise de machine learning. Por padrão, o job de machine learning analisa mensagens de log que não sejam mais antigas do que quatro semanas e continua indefinidamente.
- Adicione os índices que contêm os logs que você deseja examinar.
- Clique em Criar ML job. O job é criado e começa a rodar. Leva alguns minutos para os robôs de machine learning coletarem os dados necessários. Após o job processar os dados, você pode visualizar os resultados.

#### Analisando cateogrias dos logs

A página Categorias lista todas as categorias de log dos índices selecionados. Você pode filtrar as categorias por índices.

A captura de tela abaixo mostra as categorias do log elastic.agent.

![Logs](https://www.elastic.co/guide/en/observability/current/images/log-categories.jpg)

A linha da categoria contém as seguintes informações:

- **message count:** mostra quantas mensagens pertencem à categoria dada.
- **trend:** indica como a ocorrência das mensagens muda ao longo do tempo.
- **category name:** é o nome da categoria e é derivado do texto da mensagem.
- **datasets:** o nome dos datasets onde as categorias estão presentes.
- **maximum anomaly score:** a maior pontuação de anomalia na categoria.

Para visualizar uma mensagem de log sob uma categoria específica, clique na seta no final da linha.

Para examinar mais a fundo uma mensagem, ela pode ser visualizada no evento de log correspondente na página Stream ou exibida em seu contexto.

![Logs](https://www.elastic.co/guide/en/observability/current/images/log-opened.png)

#### Inspecionando anomalias nos logs
Quando os recursos de detecção de anomalias de machine learning estão ativados, você pode usar a página Anomalies no aplicativo Logs para detectar e inspecionar anomalias de log e as partições de log onde as anomalias ocorrem.

Isso significa que você pode facilmente ver comportamentos anômalos sem intervenção humana significativa — sem mais amostragem manual de dados de log, cálculo de taxas e determinação se as taxas são esperadas.

Anomalies destaca automaticamente períodos em que a taxa de log está fora dos limites esperados e, portanto, pode ser anômala. Por exemplo:

- Uma queda significativa na taxa de log pode sugerir que uma parte da infraestrutura parou de responder, e assim estamos atendendo menos solicitações.
- Um pico na taxa de log pode indicar um ataque DDoS. Isso pode levar a uma investigação de endereços IP de solicitações recebidas.


#### Ative a análise de taxa de log e a detecção de anomalias

Crie um job de machine learning para detectar automaticamente taxas de entrada de log anômalas.

- Selecione Anomalies, e você será solicitado a criar um job de machine learning que realizará a análise de taxa de log.
- Escolha um intervalo de tempo para a análise de machine learning.
- Adicione os Indices que contêm os logs que você deseja analisar.
- Clique em Criar ML job.
- Agora você está pronto para explorar suas partições de log.

#### Gráficos de anomalias

O gráfico Anomalies mostra uma visualização colorida e geral da taxa de entrada de log, particionada de acordo com o valor do campo event.dataset do Elastic Common Schema (ECS). Este gráfico ajuda você a identificar rapidamente aumentos ou diminuições na taxa de log de cada partição.

Se você tiver muitas partições de log, use o seguinte para filtrar seus dados:

Passe o mouse sobre um intervalo de tempo para ver a taxa de log de cada partição.

Clique ou passe o mouse sobre o nome de uma partição para mostrar, ocultar ou destacar os valores da partição.

![Logs](https://www.elastic.co/guide/en/observability/current/images/anomalies-chart.png)

O gráfico mostra o intervalo de tempo onde as anomalias foram detectadas. Os valores típicos de taxa são mostrados em cinza, enquanto as regiões anômalas são codificadas por cores e sobrepostas no topo.

Quando um intervalo de tempo é marcado como anômalo, os algoritmos de machine learning detectaram atividade incomum na taxa de log. 

Isso pode ser porque:

- A taxa de log está significativamente mais alta do que o usual.
- A taxa de log está significativamente mais baixa do que o usual.
- Outro comportamento anômalo foi detectado. Por exemplo, a taxa de log está dentro dos limites, mas não está flutuando quando se espera que esteja.

O nível de anomalia detectado em um período de tempo é codificado por cores, de vermelho, laranja, amarelo a azul. Vermelho indica um nível crítico de anomalia, enquanto azul é um nível de alerta.

Para ajudá-lo a aprofundar ainda mais em uma anomalia potencial, você pode visualizar um gráfico de anomalia para cada partição. As pontuações de anomalia variam de 0 (sem anomalias) a 100 (crítico).