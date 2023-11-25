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