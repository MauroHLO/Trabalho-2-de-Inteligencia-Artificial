2° Trabalho de Inteligência Artificial
DBSCAN – Implementação do zero em Python (NumPy)
Este repositório contém a implementação do algoritmo de agrupamento DBSCAN (Density-Based Spatial Clustering of Applications with Noise) desenvolvida como parte da 2ª atividade da disciplina de Inteligência Artificial.
O objetivo principal é compreender o funcionamento do DBSCAN por meio de uma implementação própria utilizando apenas NumPy, sem bibliotecas prontas, e analisar seu comportamento nas bases de dados solicitadas: Two Moons, Two Circles e Íris, com ênfase especial na análise da base Íris.

Estrutura do projeto
text.
├── main.py                # Script principal que executa os experimentos
├── dbscan.py              # Implementação do algoritmo DBSCAN
├── distances.py           # Funções para cálculo de distâncias (euclidiana, manhattan, chebyshev)
├── plots.py               # Funções para visualização 2D e 3D dos resultados
├── datasets.py            # Funções para carregar/gerar as bases de dados
└── README.md              # Este arquivo

Sobre o algoritmo DBSCAN
O DBSCAN é um algoritmo de agrupamento baseado em densidade que utiliza dois parâmetros principais:

ε (epsilon): raio da vizinhança de um ponto
MinPts: número mínimo de pontos dentro da vizinhança (incluindo o próprio ponto) para que um ponto seja considerado núcleo

Com base nesses parâmetros, os pontos são classificados como:

Núcleo: ≥ MinPts pontos na vizinhança
Borda: não é núcleo, mas está na vizinhança de pelo menos um núcleo
Ruído: não pertence a nenhum cluster

Clusters são formados pela expansão de pontos núcleo conectados por densidade.
Uma das principais vantagens do DBSCAN é identificar clusters de formatos arbitrários e detectar ruído automaticamente, sem precisar informar o número de clusters.

Bases de dados utilizadas
Two Moons
Base sintética com dois clusters em formato de luas crescentes (não convexos), ideal para testar a capacidade do algoritmo em estruturas não lineares.
Two Circles
Base sintética com dois círculos concêntricos, adequada para avaliar o comportamento em clusters circulares.
Íris
Base real clássica com 150 amostras, 4 atributos numéricos e 3 espécies:

Iris setosa
Iris versicolor
Iris virginica

Conforme orientado, utilizamos exclusivamente a distância euclidiana nos experimentos com a base Íris.

Metodologia

Implementação do DBSCAN do zero utilizando apenas NumPy
Suporte a três métricas de distância: euclidiana, manhattan e chebyshev (nas bases sintéticas)
Variação dos parâmetros ε e MinPts
Visualização dos resultados em 2D (núcleo/borda/ruído e clusters) e 3D (para a base Íris)
Análise qualitativa da distribuição das espécies reais nos clusters encontrados (base Íris)


Resultados e análise (Base Íris)
Visualização em 2D (comprimento da pétala × largura da pétala)

A espécie Iris setosa forma um cluster bem separado e homogêneo
As espécies versicolor e virginica apresentam sobreposição significativa
Dependendo dos valores de ε e MinPts, obtêm-se de 2 a 3 clusters, com quantidade variável de ruído (geralmente entre 5 e 20 pontos)

Visualização em 3D (comprimento da sépala + comprimento da pétala + largura da pétala)

Melhora significativa na separação visual
Iris setosa é identificada como um cluster isolado e quase puro
Versicolor e virginica ainda apresentam alguma sobreposição, mas a separação é melhor que na visualização 2D

A análise da distribuição das espécies por cluster confirma que o DBSCAN captura bem a estrutura densa de setosa, mas tem dificuldade em separar completamente as duas outras espécies devido à sobreposição natural dos dados.

Conclusão
A implementação do DBSCAN permitiu consolidar o entendimento sobre algoritmos de agrupamento baseados em densidade, evidenciando suas principais vantagens:

Capacidade de identificar clusters de formatos arbitrários
Detecção automática de ruído
Não exige definição prévia do número de clusters

Ao mesmo tempo, revelou limitações importantes:

Alta sensibilidade à escolha dos parâmetros ε e MinPts
Desempenho inferior em dados com sobreposição significativa entre classes

Na base Íris, o algoritmo se mostrou particularmente eficaz para identificar Iris setosa, mas as espécies versicolor e virginica exigem maior cuidado na escolha dos parâmetros e das dimensões analisadas.
De modo geral, o DBSCAN provou ser uma abordagem robusta e flexível, especialmente útil em cenários reais onde a detecção de outliers e a descoberta de estruturas densas são prioridades.

Como executar

Certifique-se de ter as dependências instaladas:Bashpip install numpy matplotlib scikit-learn
Execute o script principal:Bashpython main.py

Os gráficos serão exibidos automaticamente e informações úteis para o relatório da base Íris serão impressas no console.
