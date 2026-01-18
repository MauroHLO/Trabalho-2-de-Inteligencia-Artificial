# Relatório – Algoritmo DBSCAN aplicado à Base Íris

## 1. Introdução

Este trabalho tem como objetivo a implementação do algoritmo de agrupamento **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**, conforme apresentado em sala de aula, e sua aplicação em diferentes bases de dados. O foco principal do relatório é a análise dos resultados obtidos na **base Íris**, comparando os agrupamentos encontrados pelo algoritmo com a classificação real das espécies.

O DBSCAN se destaca por ser um algoritmo baseado em densidade, capaz de identificar clusters de formatos arbitrários e detectar pontos considerados ruído, não exigindo a definição prévia do número de clusters.

---

## 2. Visão geral do DBSCAN

O funcionamento do DBSCAN depende de dois parâmetros principais:

- **ε (epsilon):** raio da vizinhança de um ponto;
- **MinPts:** número mínimo de pontos necessários dentro da vizinhança para que um ponto seja considerado um ponto núcleo.

A partir desses parâmetros, os pontos são classificados em:
- **Pontos Núcleo:** possuem pelo menos `MinPts` pontos em sua vizinhança;
- **Pontos de Borda:** não são núcleo, mas estão na vizinhança de um ponto núcleo;
- **Pontos de Ruído:** não pertencem a nenhum cluster.

Clusters são formados pela expansão de pontos núcleo conectados por densidade.

---

## 3. Base de dados Íris

A base **Íris** é composta por 150 amostras, cada uma descrita por quatro atributos numéricos:

- Comprimento da sépala
- Largura da sépala
- Comprimento da pétala
- Largura da pétala

As amostras pertencem a três espécies:
- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

Conforme sugerido no enunciado, foi utilizada a **distância euclidiana** para os experimentos com essa base.

---

## 4. Metodologia

Para aplicar o DBSCAN à base Íris, foram realizados testes com diferentes valores de `ε` e `MinPts`, observando-se visualmente os resultados por meio de gráficos bidimensionais e tridimensionais.

Os principais passos adotados foram:
1. Seleção de pares de atributos (2D) e trios de atributos (3D);
2. Execução do DBSCAN com diferentes configurações de parâmetros;
3. Visualização dos pontos classificados como núcleo, borda e ruído;
4. Comparação qualitativa dos clusters encontrados com as espécies reais da base.

Cabe ressaltar que o DBSCAN não é um algoritmo supervisionado, portanto a comparação com as classes reais tem caráter apenas analítico e interpretativo.

---

## 5. Resultados obtidos

### 5.1 Visualização em duas dimensões

Ao utilizar atributos relacionados às pétalas (comprimento e largura), observou-se que o DBSCAN consegue formar agrupamentos coerentes para parte dos dados, especialmente para a espécie *Iris setosa*, que apresenta maior separabilidade em relação às demais.

Entretanto, as espécies *Iris versicolor* e *Iris virginica* apresentam regiões de sobreposição, o que dificulta uma separação clara baseada apenas em densidade, resultando em:
- clusters mistos;
- presença de pontos classificados como ruído, dependendo do valor de `ε`.

### 5.2 Visualização em três dimensões

A utilização de três atributos simultaneamente melhora a separação visual dos dados. Em alguns testes, foi possível observar clusters mais bem definidos, embora ainda exista sobreposição entre *versicolor* e *virginica*.

Esse comportamento evidencia uma característica importante do DBSCAN: sua sensibilidade à escolha dos parâmetros e à escala dos dados.

---

## 6. Discussão

Os experimentos mostram que o DBSCAN:
- é eficiente para identificar regiões densas e detectar ruído;
- não exige a definição prévia do número de clusters;
- apresenta desempenho dependente da escolha adequada de `ε` e `MinPts`.

Na base Íris, o algoritmo se mostrou particularmente eficaz para identificar a espécie *Iris setosa*, enquanto as demais espécies apresentam padrões de densidade mais complexos, o que dificulta uma separação perfeita.

A presença de pontos classificados como ruído não representa necessariamente um erro do algoritmo, mas sim uma consequência natural de regiões de baixa densidade ou de transição entre clusters.

---

## 7. Conclusão

A implementação do DBSCAN permitiu compreender, de forma prática, o funcionamento de algoritmos de agrupamento baseados em densidade. A aplicação à base Íris evidenciou tanto as vantagens quanto as limitações do método, especialmente em conjuntos de dados com sobreposição entre classes.

De modo geral, o DBSCAN mostrou-se uma abordagem robusta e flexível, sendo particularmente útil em cenários onde a detecção de ruído e a identificação de clusters de formatos arbitrários são desejáveis.