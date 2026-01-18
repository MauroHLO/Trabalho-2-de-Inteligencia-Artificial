import numpy as np
from dataclasses import dataclass
from typing import Callable, Optional, Tuple, Literal
from distances import get_distance_matrix

PointType = Literal["core", "border", "noise"]

def pairwise_distances(X: np.ndarray, metric: str = "euclidean") -> np.ndarray:
    """
    Calcula a matriz de distâncias NxN usando NumPy (vetorizado).
    metric: 'euclidean', 'manhattan', 'chebyshev'
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X deve ser 2D (n_amostras, n_features).")

    # shape: (N, 1, D) e (1, N, D) -> broadcast para (N, N, D)
    diff = X[:, None, :] - X[None, :, :]

    if metric == "euclidean":
        # sqrt(sum(diff^2))
        return np.sqrt(np.sum(diff * diff, axis=2))
    elif metric == "manhattan":
        # sum(|diff|)
        return np.sum(np.abs(diff), axis=2)
    elif metric == "chebyshev":
        # max(|diff|)
        return np.max(np.abs(diff), axis=2)
    else:
        raise ValueError(f"Métrica '{metric}' não suportada.")

def custom_pairwise_distances(X: np.ndarray, metric_fn: Callable[[np.ndarray, np.ndarray], float]) -> np.ndarray:
    """
    Matriz de distâncias NxN com uma métrica custom (mais lenta, mas flexível).
    metric_fn(a, b) -> float
    """
    X = np.asarray(X, dtype=float)
    n = X.shape[0]
    D = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(i, n):
            d = float(metric_fn(X[i], X[j]))
            D[i, j] = d
            D[j, i] = d
    return D

@dataclass
class DBSCANResult:
    labels: np.ndarray        # shape (N,), -1 = ruído, 0..K-1 clusters
    point_type: np.ndarray    # shape (N,), strings: 'core'/'border'/'noise'

def dbscan(
    X: np.ndarray,
    eps: float,
    min_samples: int,
    metric: str = "euclidean",
    metric_fn: Optional[Callable[[np.ndarray, np.ndarray], float]] = None,
    include_self: bool = True
) -> DBSCANResult:
    """
    Implementação DBSCAN do zero (NumPy).

    Parâmetros:
      - eps: raio da vizinhança
      - min_samples: mínimo de pontos na vizinhança para ser núcleo
      - metric: 'euclidean' | 'manhattan' | 'chebyshev' (ignorado se metric_fn for passado)
      - metric_fn: função de distância custom (se passada, usa ela)
      - include_self: se True, conta o próprio ponto na vizinhança (padrão DBSCAN clássico)

    Retorna:
      - labels: cluster id para cada ponto (-1 ruído)
      - point_type: 'core', 'border', 'noise'
    """
    X = np.asarray(X, dtype=float)
    if eps <= 0:
        raise ValueError("eps deve ser > 0.")
    if min_samples < 1:
        raise ValueError("min_samples deve ser >= 1.")
    n = X.shape[0]
    if n == 0:
        return DBSCANResult(labels=np.array([], dtype=int), point_type=np.array([], dtype=object))

    # 1) Distâncias
    dist = get_distance_matrix(X, metric=metric, metric_fn=metric_fn)

    # 2) Vizinhança: neighbors[i] = índices dos pontos com dist <= eps
    within = dist <= eps
    if not include_self:
        np.fill_diagonal(within, False)

    neighbors = [np.flatnonzero(within[i]) for i in range(n)]
    neighbor_counts = np.array([len(nb) for nb in neighbors], dtype=int)

    # 3) Núcleo: >= min_samples (considerando include_self conforme acima)
    is_core = neighbor_counts >= min_samples

    # Inicializações
    UNVISITED = 0
    VISITED = 1
    state = np.zeros(n, dtype=np.uint8)

    labels = np.full(n, -1, dtype=int)          # -1: ruído
    point_type = np.full(n, "noise", dtype=object)

    cluster_id = 0

    # 4) Expansão de clusters
    for i in range(n):
        if state[i] == VISITED:
            continue

        state[i] = VISITED

        # Se não é núcleo, por enquanto marca como ruído (pode virar borda depois)
        if not is_core[i]:
            continue

        # Começa um novo cluster
        labels[i] = cluster_id
        point_type[i] = "core"

        # Fila de expansão (BFS)
        queue = list(neighbors[i])

        while queue:
            j = queue.pop()

            if state[j] == UNVISITED:
                state[j] = VISITED

                # Se j é núcleo, adiciona seus vizinhos para expandir
                if is_core[j]:
                    point_type[j] = "core"
                    # adiciona vizinhos (pode repetir, mas funciona; dá pra otimizar com set)
                    queue.extend(neighbors[j])

            # Se ainda não tem cluster, atribui ao cluster atual
            if labels[j] == -1:
                labels[j] = cluster_id
                # Se não for núcleo, é borda (conectado a um núcleo)
                if not is_core[j]:
                    point_type[j] = "border"
                else:
                    point_type[j] = "core"

        cluster_id += 1

    # Pós-processamento: qualquer núcleo marcado corretamente já está ok.
    # Quem ficou -1 é ruído (noise). Quem tem cluster e não é core vira border.
    # (o código acima já faz isso, mas garantimos consistência)
    point_type[(labels != -1) & (~is_core)] = "border"
    point_type[(labels == -1)] = "noise"
    point_type[(labels != -1) & (is_core)] = "core"

    return DBSCANResult(labels=labels, point_type=point_type)
