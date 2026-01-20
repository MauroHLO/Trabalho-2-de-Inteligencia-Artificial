# DBSCAN – Implementação em Python (NumPy)

**2º Trabalho da disciplina de Inteligência Artificial**

Este repositório apresenta uma implementação **do zero** do algoritmo de agrupamento **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**, desenvolvida utilizando exclusivamente a biblioteca **NumPy**, sem o uso de bibliotecas prontas de clustering.

O objetivo do trabalho é compreender o funcionamento interno do DBSCAN e analisar seu comportamento em diferentes bases de dados, com foco especial na base **Íris**.

---

## Estrutura do Projeto

```
├── main.py         # Script principal de execução
├── dbscan.py       # Implementação do algoritmo DBSCAN
├── distances.py    # Métricas de distância (euclidiana, manhattan, chebyshev)
├── plots.py        # Funções de visualização 2D e 3D
├── datasets.py     # Carregamento e geração das bases de dados
└── relatorio.md    # Documentação do projeto

```

---

## Sobre o DBSCAN

O DBSCAN é um algoritmo de agrupamento baseado em densidade que utiliza dois parâmetros principais:

- **ε (epsilon)**: raio da vizinhança de um ponto  
- **MinPts**: número mínimo de pontos na vizinhança para que um ponto seja considerado núcleo  

Com base nesses parâmetros, os pontos são classificados como:

- **Núcleo**: possui pelo menos *MinPts* pontos na vizinhança  
- **Borda**: não é núcleo, mas está na vizinhança de um ponto núcleo  
- **Ruído**: não pertence a nenhum cluster  

Uma das principais vantagens do DBSCAN é a capacidade de identificar **clusters de formatos arbitrários** e detectar **ruído automaticamente**, sem exigir a definição prévia do número de clusters.

---

## Bases de Dados Utilizadas

- **Two Moons**  
  Base sintética com clusters não convexos, usada para avaliar o comportamento do algoritmo em estruturas não lineares.

- **Two Circles**  
  Base sintética com dois círculos concêntricos, utilizada para testar agrupamentos circulares.

- **Íris**  
  Base real clássica com 150 amostras, 4 atributos numéricos e 3 espécies:
  - Iris setosa  
  - Iris versicolor  
  - Iris virginica  

Nos experimentos com a base Íris, foi utilizada **exclusivamente a distância euclidiana**, conforme orientação do trabalho.

---

## Metodologia

- Implementação completa do DBSCAN utilizando apenas NumPy  
- Suporte a múltiplas métricas de distância (bases sintéticas)  
- Variação dos parâmetros ε e MinPts  
- Visualização dos resultados:
  - 2D: clusters, pontos núcleo, borda e ruído  
  - 3D: análise da base Íris  
- Análise qualitativa da distribuição das espécies reais nos clusters obtidos

---

## Resultados – Base Íris

Na visualização 2D (comprimento × largura da pétala), a espécie **Iris setosa** forma um cluster bem definido e homogêneo, enquanto **versicolor** e **virginica** apresentam sobreposição significativa. Dependendo dos valores de ε e MinPts, são obtidos de dois a três clusters, com presença variável de ruído.

Na visualização 3D (combinação de atributos da sépala e pétala), observa-se uma melhora na separação visual. A espécie **setosa** permanece claramente isolada, enquanto **versicolor** e **virginica** continuam parcialmente sobrepostas, porém com melhor distinção em relação à visualização 2D.

Esses resultados indicam que o DBSCAN captura bem regiões densas bem definidas, mas encontra limitações quando há sobreposição natural entre classes.

---

## Conclusão

A implementação do DBSCAN permitiu aprofundar o entendimento sobre algoritmos de agrupamento baseados em densidade, evidenciando vantagens como:

- Identificação de clusters de formatos arbitrários  
- Detecção automática de ruído  
- Independência do número prévio de clusters  

Por outro lado, o algoritmo mostrou alta sensibilidade à escolha dos parâmetros ε e MinPts, além de desempenho limitado em dados com grande sobreposição entre classes.

Na base Íris, o DBSCAN foi especialmente eficaz na identificação da espécie **Iris setosa**, enquanto **versicolor** e **virginica** exigem ajustes cuidadosos de parâmetros e dimensionalidade.

---

## Como Executar

Instale as dependências:

```bash
pip install numpy matplotlib scikit-learn
```

e rode o script principal
```
python main.py
