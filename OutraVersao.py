import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles, load_iris
from scipy.spatial.distance import euclidean
import pandas as pd


class MyDBSCAN:
    def __init__(self, eps, min_pts):
        self.eps = eps
        self.min_pts = min_pts
        self.labels = None  # IDs dos clusters (-1 para ruído)
        self.point_types = None  # Núcleo, Borda, Ruído

    def fit(self, X):
        n_samples = X.shape[0]
        self.labels = np.full(n_samples, -1)  # Inicializa todos como ruído
        self.point_types = np.full(n_samples, "Ruído", dtype=object)

        # 1. Pré-calcular vizinhos
        neighbors_list = [
            np.where(np.array([euclidean(X[i], X[j]) for j in range(n_samples)]) <= self.eps)[0]
            for i in range(n_samples)
        ]

        # 2. Identificar Núcleos
        core_indices = [i for i, neighbors in enumerate(neighbors_list) if len(neighbors) >= self.min_pts]
        for idx in core_indices:
            self.point_types[idx] = "Núcleo"

        # 3. Identificar Clusters e Bordas
        cluster_id = 0
        visited = set()

        for i in core_indices:
            if i not in visited:
                # Inicia a expansão de um novo cluster
                visited.add(i)
                self.labels[i] = cluster_id
                queue = list(neighbors_list[i])

                idx_q = 0
                while idx_q < len(queue):
                    neighbor_idx = queue[idx_q]
                    idx_q += 1

                    if neighbor_idx not in visited:
                        visited.add(neighbor_idx)
                        self.labels[neighbor_idx] = cluster_id

                        # Se o vizinho também for núcleo, expande por ele
                        if neighbor_idx in core_indices:
                            queue.extend(neighbors_list[neighbor_idx])
                        else:
                            # Se não é núcleo mas foi alcançado por um, é Borda
                            self.point_types[neighbor_idx] = "Borda"

                cluster_id += 1

        return self.point_types, self.labels


# Função de plotagem para visualizar Clusters vs Tipos de Pontos
def plot_results(X, types, labels, title):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # Gráfico 1: Tipos de Pontos (Núcleo, Borda, Ruído) conforme pedido [cite: 12, 13]
    colors_types = {'Núcleo': 'red', 'Borda': 'blue', 'Ruído': 'green'}
    for t in np.unique(types):
        idx = np.where(types == t)
        ax1.scatter(X[idx, 0], X[idx, 1], c=colors_types[t], label=t, edgecolors='k')
    ax1.set_title(f"{title}: Classificação de Pontos")
    ax1.legend()

    # Gráfico 2: Clusters Identificados
    scatter = ax2.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')
    ax2.set_title(f"{title}: Clusters Identificados")
    plt.show()


# --- Execução para as bases solicitadas ---

# 1. Duas Luas [cite: 9, 15]
X_moons, _ = make_moons(n_samples=300, noise=0.08, random_state=42)
db_moons = MyDBSCAN(eps=0.2, min_pts=5)
types_m, labels_m = db_moons.fit(X_moons)
plot_results(X_moons, types_m, labels_m, "Two Moons")

# 2. Dois Círculos [cite: 10, 46]
X_circles, _ = make_circles(n_samples=300, factor=0.5, noise=0.05, random_state=42)
db_circles = MyDBSCAN(eps=0.25, min_pts=5)
types_c, labels_c = db_circles.fit(X_circles)
plot_results(X_circles, types_c, labels_c, "Two Circles")

# 1. Carregar a base Íris [cite: 11, 76]
iris = load_iris()
X_iris = iris.data
y_real = iris.target

# 2. Executar o DBSCAN (ajustando eps e min_pts para 2D)
# Usando Distância Euclidiana conforme exigido
modelo_2d = MyDBSCAN(eps=0.55, min_pts=5)
tipos, clusters = modelo_2d.fit(X_iris)

# 3. Preparar dados para o gráfico 2D
# Usaremos as colunas 0 e 1 (Sepal Length e Sepal Width)
plt.figure(figsize=(10, 6))

colors = {'Núcleo': 'red', 'Borda': 'blue', 'Ruído': 'green'}

for t in ['Núcleo', 'Borda', 'Ruído']:
    idx = [i for i, v in enumerate(tipos) if v == t]
    if idx:
        plt.scatter(X_iris[idx, 0], X_iris[idx, 1],
                    c=colors[t], label=t, edgecolors='k', s=60)

plt.title("DBSCAN Íris 2D: Identificação de Núcleo, Borda e Ruído ")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
