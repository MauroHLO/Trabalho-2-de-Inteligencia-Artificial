2º Trabalho de Inteligência Artificial
DBSCAN – Implementação do zero em Python (NumPy)

Este repositório contém a implementação do algoritmo de agrupamento DBSCAN (Density-Based Spatial Clustering of Applications with Noise) desenvolvida como parte da 2ª atividade da disciplina de Inteligência Artificial.

O objetivo principal é compreender o funcionamento do DBSCAN por meio de uma implementação própria, utilizando apenas NumPy, sem recorrer a bibliotecas prontas de clustering, além de analisar seu comportamento nas bases de dados solicitadas:

Two Moons

Two Circles

Íris

Com ênfase especial na análise da base Íris.

📁 Estrutura do projeto
.
├── main.py                # Script principal que executa os experimentos
├── dbscan.py              # Implementação do algoritmo DBSCAN
├── distances.py           # Funções para cálculo de distâncias
│                           # (euclidiana, manhattan, chebyshev)
├── plots.py               # Funções para visualização 2D e 3D dos resultados
├── datasets.py            # Funções para carregar/gerar as bases de dados
└── README.md              # Este arquivo

📌 Sobre o algoritmo DBSCAN

O DBSCAN é um algoritmo de agrupamento baseado em densidade que utiliza dois parâmetros principais:

ε (epsilon): raio da vizinhança de um ponto

MinPts: número mínimo de pontos dentro da vizinhança (incluindo o próprio ponto) para que um ponto seja considerado núcleo

Com base nesses parâmetros, os pontos são classificados como:

Núcleo: possui ≥ MinPts pontos na vizinhança

Borda: não é núcleo, mas está na vizinhança de pelo menos um ponto núcleo

Ruído: não pertence a nenhum cluster

Os clusters são formados pela expansão de pontos núcleo conectados por densidade.

Principais vantagens do DBSCAN

Identifica clusters de formatos arbitrários

Detecta ruído automaticamente

Não exige a definição prévia do número de clusters

📊 Bases de dados utilizadas
Two Moons

Base sintética com dois clusters em formato de luas crescentes (não convexos), ideal para testar a capacidade do algoritmo em lidar com estruturas não lineares.

Two Circles

Base sintética composta por dois círculos concêntricos, utilizada para avaliar o comportamento do algoritmo em clusters circulares.

Íris

Base real clássica com:

150 amostras

4 atributos numéricos

3 espécies:

Iris setosa

Iris versicolor

Iris virginica

Conforme orientado, foi utilizada exclusivamente a distância euclidiana nos experimentos com a base Íris.

⚙️ Metodologia

Implementação do DBSCAN do zero utilizando apenas NumPy

Suporte a três métricas de distância:

Euclidiana

Manhattan

Chebyshev
(utilizadas nas bases sintéticas)

Variação dos parâmetros ε e MinPts

Visualização dos resultados:

2D: clusters, pontos núcleo, borda e ruído

3D: visualização da base Íris

Análise qualitativa da distribuição das espécies reais nos clusters obtidos (base Íris)

📈 Resultados e análise — Base Íris
Visualização em 2D

(Comprimento da pétala × largura da pétala)

A espécie Iris setosa forma um cluster bem separado e homogêneo

As espécies versicolor e virginica apresentam sobreposição significativa

Dependendo dos valores de ε e MinPts, obtêm-se:

De 2 a 3 clusters

Quantidade variável de ruído (geralmente entre 5 e 20 pontos)

Visualização em 3D

(Comprimento da sépala + comprimento da pétala + largura da pétala)

Há uma melhora significativa na separação visual

Iris setosa é identificada como um cluster isolado e quase puro

Versicolor e virginica ainda apresentam alguma sobreposição, porém menor que na visualização 2D

A análise da distribuição das espécies por cluster confirma que o DBSCAN captura bem a estrutura densa da setosa, mas encontra dificuldades para separar completamente as outras duas espécies devido à sobreposição natural dos dados.

✅ Conclusão

A implementação do DBSCAN permitiu consolidar o entendimento sobre algoritmos de agrupamento baseados em densidade, evidenciando suas principais vantagens:

Capacidade de identificar clusters de formatos arbitrários

Detecção automática de ruído

Não exige definição prévia do número de clusters

Ao mesmo tempo, revelou limitações importantes:

Alta sensibilidade à escolha dos parâmetros ε e MinPts

Desempenho inferior em dados com sobreposição significativa entre classes

Na base Íris, o algoritmo mostrou-se particularmente eficaz para identificar a espécie Iris setosa, enquanto versicolor e virginica exigem maior cuidado na escolha dos parâmetros e das dimensões analisadas.

De forma geral, o DBSCAN se mostrou uma abordagem robusta e flexível, especialmente útil em cenários reais onde a detecção de outliers e a descoberta de estruturas densas são prioridades.

▶️ Como executar
Dependências

Certifique-se de ter as dependências instaladas:

pip install numpy matplotlib scikit-learn


Execução

Execute o script principal:

python main.py


Os gráficos serão exibidos automaticamente e informações relevantes para a análise da base Íris serão impressas no console.
