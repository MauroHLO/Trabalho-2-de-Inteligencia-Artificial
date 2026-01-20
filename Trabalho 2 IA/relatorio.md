# Relatório – Algoritmo DBSCAN aplicado à Base Íris

## 1. Introdução

Este trabalho apresenta a implementação do algoritmo de agrupamento **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**, conforme apresentado em sala de aula, e sua aplicação nas bases de dados solicitadas: **Two Moons**, **Two Circles** e **Íris**.

O foco principal deste relatório é a análise dos resultados obtidos na **base Íris**, comparando os agrupamentos encontrados pelo algoritmo com a classificação real das espécies (*Iris setosa*, *Iris versicolor* e *Iris virginica*).

O DBSCAN é um algoritmo baseado em densidade que identifica clusters de formatos arbitrários e detecta pontos de ruído, sem a necessidade de informar previamente o número de clusters.

---

## 2. Visão geral do DBSCAN

O funcionamento do DBSCAN depende de dois parâmetros principais:

- **ε (epsilon):** raio da vizinhança de um ponto;
- **MinPts:** número mínimo de pontos necessários na vizinhança para que um ponto seja considerado núcleo.

Os pontos são classificados em:
- **Pontos Núcleo:** ≥ MinPts pontos na vizinhança (incluindo o próprio ponto);
- **Pontos de Borda:** não são núcleo, mas pertencem à vizinhança de pelo menos um ponto núcleo;
- **Pontos de Ruído:** não pertencem a nenhum cluster.

Clusters são formados pela expansão de pontos núcleo conectados por densidade.

---

## 3. Base de dados Íris

A base **Íris** contém 150 amostras, cada uma descrita por quatro atributos numéricos:

- Comprimento da sépala (sepal length)
- Largura da sépala (sepal width)
- Comprimento da pétala (petal length)
- Largura da pétala (petal width)

As amostras pertencem a três espécies:
- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

Conforme orientado no enunciado, utilizamos a **distância euclidiana** para todos os experimentos com a base Íris.

---

## 4. Metodologia

Foram realizados testes com diferentes valores de `ε` e `MinPts`, utilizando:

- **Visualização 2D:** comprimento da pétala vs. largura da pétala (atributos 2 e 3);
- **Visualização 3D:** comprimento da sépala, comprimento da pétala e largura da pétala (atributos 0, 2 e 3).

Para cada configuração:
1. Execução do DBSCAN;
2. Plotagem dos pontos coloridos por tipo (núcleo, borda, ruído);
3. Plotagem dos clusters formados (ruído marcado como -1);
4. Análise qualitativa da distribuição das espécies reais por cluster.

Também foram testadas as bases **Two Moons** e **Two Circles** com diferentes métricas de distância (euclidiana, manhattan e chebyshev) para verificar o comportamento do algoritmo em dados com formatos não convexos.

---

## 5. Resultados obtidos

### 5.1 Bases Two Moons e Two Circles

Nas bases sintéticas **Two Moons** e **Two Circles**, o algoritmo conseguiu identificar corretamente os dois clusters de formato não convexo, especialmente com a métrica euclidiana e valores adequados de `ε` e `MinPts`. As outras métricas (manhattan e chebyshev) também foram testadas com bons resultados, ajustando-se os parâmetros de acordo com a escala de cada métrica.

Os pontos de ruído foram poucos ou inexistentes nas configurações bem escolhidas, demonstrando a capacidade do DBSCAN de lidar com clusters de formas complexas.

### 5.2 Visualização em duas dimensões (Íris)

Ao utilizar os atributos **comprimento da pétala** e **largura da pétala** (colunas 2 e 3), observou-se:

- A espécie *Iris setosa* forma um cluster bem separado;
- As espécies *Iris versicolor* e *Iris virginica* apresentam sobreposição significativa, resultando em clusters mistos ou em alguns pontos classificados como ruído;
- Valores de `ε` entre 0.35 e 0.60 com `MinPts = 5` geraram diferentes quantidades de clusters (geralmente 2 a 3) e ruído (entre 5 e 20 pontos).

### 5.3 Visualização em três dimensões (Íris)

Ao utilizar três atributos (**comprimento da sépala**, **comprimento da pétala** e **largura da pétala** — colunas 0, 2 e 3), com `ε = 0.55` e `MinPts = 5`, obteve-se:

- Separação visual mais clara dos clusters;
- A espécie *Iris setosa* foi perfeitamente identificada como um cluster isolado;
- As espécies *versicolor* e *virginica* ainda apresentam alguma sobreposição, mas a separação é melhor que na visualização 2D.

A análise da distribuição das espécies por cluster mostrou que:
- O cluster principal de *setosa* é quase puro;
- Os clusters de *versicolor* e *virginica* são mistos, com alguns pontos de transição classificados como ruído ou borda.

---

## 6. Discussão

Os experimentos confirmam que o DBSCAN:

- É eficiente na detecção de regiões densas e na identificação de ruído;
- Não exige a definição prévia do número de clusters;
- É sensível à escolha de `ε` e `MinPts`, exigindo ajustes visuais e experimentais;

Na base Íris, o algoritmo identificou bem a espécie *Iris setosa*, mas teve dificuldade em separar completamente *versicolor* e *virginica* devido à sobreposição natural dos dados. Isso é esperado, pois o DBSCAN não é um classificador supervisionado, mas um algoritmo de agrupamento baseado em densidade.

A presença de pontos de ruído e borda reflete regiões de baixa densidade ou de transição entre as espécies.

---

## 7. Conclusão

A implementação do DBSCAN permitiu compreender na prática o funcionamento de algoritmos de agrupamento baseados em densidade. A aplicação à base Íris revelou tanto as vantagens (detecção de ruído, clusters de formato arbitrário) quanto as limitações (sensibilidade aos parâmetros e dificuldade em separar classes com sobreposição).

De forma geral, o algoritmo mostrou-se robusto e flexível, sendo especialmente útil em cenários onde a detecção de outliers e a descoberta de estruturas densas são importantes.