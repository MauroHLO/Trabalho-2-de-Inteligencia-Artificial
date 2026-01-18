from __future__ import annotations
import numpy as np
from typing import Callable, Optional, Literal

MetricName = Literal["euclidean", "manhattan", "chebyshev"]


def pairwise_distances(X: np.ndarray, metric: MetricName = "euclidean") -> np.ndarray:
    """
    Calcula a matriz de distâncias NxN usando NumPy (vetorizado).

    Parâmetros:
      - X: array (N, D)
      - metric: 'euclidean' | 'manhattan' | 'chebyshev'

    Retorna:
      - dist: array (N, N) com distâncias entre todos os pares
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X deve ser 2D (n_amostras, n_features).")

    diff = X[:, None, :] - X[None, :, :]  # (N, N, D)

    if metric == "euclidean":
        return np.sqrt(np.sum(diff * diff, axis=2))
    if metric == "manhattan":
        return np.sum(np.abs(diff), axis=2)
    if metric == "chebyshev":
        return np.max(np.abs(diff), axis=2)

    raise ValueError(f"Métrica '{metric}' não suportada.")


def custom_pairwise_distances(
    X: np.ndarray,
    metric_fn: Callable[[np.ndarray, np.ndarray], float],
) -> np.ndarray:
    """
    Matriz de distâncias NxN com métrica custom (O(N^2) com loops).

    Use quando:
      - você quer testar uma distância que não está no conjunto padrão.

    Parâmetros:
      - X: array (N, D)
      - metric_fn: função (a, b) -> float

    Retorna:
      - dist: array (N, N)
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X deve ser 2D (n_amostras, n_features).")

    n = X.shape[0]
    dist = np.empty((n, n), dtype=float)

    for i in range(n):
        dist[i, i] = 0.0
        for j in range(i + 1, n):
            d = float(metric_fn(X[i], X[j]))
            dist[i, j] = d
            dist[j, i] = d

    return dist


def get_distance_matrix(
    X: np.ndarray,
    metric: MetricName = "euclidean",
    metric_fn: Optional[Callable[[np.ndarray, np.ndarray], float]] = None,
) -> np.ndarray:
    """
    Conveniência: se metric_fn vier, usa custom; senão usa metric padrão.
    """
    if metric_fn is not None:
        return custom_pairwise_distances(X, metric_fn)
    return pairwise_distances(X, metric=metric)