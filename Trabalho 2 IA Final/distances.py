from __future__ import annotations
import numpy as np
from typing import Literal

MetricaNome = Literal["euclidiano", "manhattan", "chebyshev"]


def distancia_entre_pares(X: np.ndarray, metrica: MetricaNome = "euclidiano") -> np.ndarray:
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X deve ser 2D (n_amostras, n_features).")

    dif = X[:, None, :] - X[None, :, :]  # (N, N, D)

    if metrica == "euclidiano":
        return np.sqrt(np.sum(dif * dif, axis=2))
    if metrica == "manhattan":
        return np.sum(np.abs(dif), axis=2)
    if metrica == "chebyshev":
        return np.max(np.abs(dif), axis=2)

    raise ValueError(f"Métrica '{metrica}' não suportada.")


def get_matriz_distancia(
    X: np.ndarray,
    metrica: MetricaNome = "euclidiano",
) -> np.ndarray:
    return distancia_entre_pares(X, metrica=metrica)