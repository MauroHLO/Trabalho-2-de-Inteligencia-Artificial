# 2-Trabalho-de-Intelig-ncia-Artificial
# DBSCAN – Implementação do zero em Python (NumPy)

Este repositório contém a implementação do algoritmo de agrupamento **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** desenvolvida como parte da 2ª atividade da disciplina de Inteligência Artificial.

O objetivo principal é compreender o funcionamento do DBSCAN por meio de uma implementação própria, bem como analisar seu comportamento em diferentes bases de dados, com foco especial na base **Íris**.

---

## 📌 Estrutura do projeto


---

## 🧠 Sobre o algoritmo DBSCAN

O DBSCAN é um algoritmo de agrupamento baseado em densidade que utiliza dois parâmetros principais:

- **ε (epsilon):** raio da vizinhança de um ponto;
- **MinPts:** número mínimo de pontos dentro da vizinhança para que um ponto seja considerado núcleo.

Com base nesses parâmetros, os pontos são classificados como:
- **Núcleo:** pontos em regiões densas;
- **Borda:** pontos próximos a núcleos, mas que não atendem ao critério de densidade;
- **Ruído:** pontos isolados ou em regiões de baixa densidade.

Uma das principais vantagens do DBSCAN é a capacidade de identificar clusters de formatos arbitrários e detectar ruído, sem a necessidade de definir previamente o número de clusters.

---

## 📊 Bases de dados utilizadas

### • Two Moons
Base sintética com dois clusters em formato não linear, utilizada para avaliar a capacidade do DBSCAN de identificar agrupamentos de formatos arbitrários.

### • Two Circles
Base sintética composta por dois círculos concêntricos, adequada para testar o comportamento do algoritmo em estruturas circulares.

### • Íris
Base real composta por 150 amostras, com quatro atributos numéricos relacionados às flores e três espécies distintas:
- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

Conforme sugerido no enunciado da atividade, foi utilizada a **distância euclidiana** para os experimentos com a base Íris.

---

## 🔬 Metodologia

Os experimentos foram conduzidos variando-se os parâmetros `ε` e `MinPts`, bem como o critério de distância nas bases sintéticas. Para a base Íris, foram realizadas visualizações em duas e três dimensões, permitindo uma análise qualitativa dos agrupamentos obtidos.

O algoritmo foi implementado do zero utilizando **NumPy**, sem o uso de implementações prontas de DBSCAN.

---

## 📈 Resultados e análise (Base Íris)

Os resultados mostram que o DBSCAN é capaz de identificar agrupamentos coerentes para parte da base Íris, especialmente para a espécie *Iris setosa*, que apresenta maior separabilidade em relação às demais.

As espécies *Iris versicolor* e *Iris virginica* apresentam regiões de sobreposição, o que dificulta uma separação clara baseada apenas em densidade, resultando em clusters mistos e, em alguns casos, pontos classificados como ruído.

A utilização de três atributos simultaneamente melhora a separação visual dos dados, evidenciando a importância da escolha das dimensões e dos parâmetros do algoritmo.

Cabe ressaltar que o DBSCAN é um método não supervisionado, portanto a comparação com as classes reais tem caráter analítico e não representa uma medida de acurácia.

---

## ✅ Conclusão

A implementação do DBSCAN permitiu consolidar o entendimento sobre algoritmos de agrupamento baseados em densidade, evidenciando tanto suas vantagens quanto limitações.

De modo geral, o DBSCAN mostrou-se uma abordagem robusta e flexível, especialmente útil em cenários onde a detecção de ruído e a identificação de clusters de formatos arbitrários são desejáveis.

---
