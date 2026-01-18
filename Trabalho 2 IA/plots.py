# plots.py
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Sequence, Literal, Tuple

PointType = Literal["core", "border", "noise"]


def _ensure_numpy_1d(arr, name: str) -> np.ndarray:
    arr = np.asarray(arr)
    if arr.ndim != 1:
        raise ValueError(f"{name} deve ser 1D.")
    return arr


def plot_point_types_2d(
    X: np.ndarray,
    point_type: Sequence[PointType],
    title: str = "DBSCAN - Tipos de ponto",
    feature_names: Optional[Tuple[str, str]] = None,
    figsize: Tuple[int, int] = (7, 6),
    alpha: float = 0.85,
    s: int = 40,
    show: bool = True,
    savepath: Optional[str] = None,
) -> None:
    """
    Plota um scatter 2D colorindo por tipo de ponto: core / border / noise.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or X.shape[1] < 2:
        raise ValueError("X precisa ser 2D e ter pelo menos 2 colunas para plot 2D.")

    pt = np.asarray(point_type, dtype=object)
    if pt.shape[0] != X.shape[0]:
        raise ValueError("point_type deve ter o mesmo tamanho que X.")

    x0, x1 = X[:, 0], X[:, 1]

    fig = plt.figure(figsize=figsize)
    ax = plt.gca()

    mask_core = (pt == "core")
    mask_border = (pt == "border")
    mask_noise = (pt == "noise")

    ax.scatter(x0[mask_core], x1[mask_core], label="Núcleo", s=s, alpha=alpha, marker="o")
    ax.scatter(x0[mask_border], x1[mask_border], label="Borda", s=s, alpha=alpha, marker="^")
    ax.scatter(x0[mask_noise], x1[mask_noise], label="Ruído", s=s, alpha=alpha, marker="x")

    ax.set_title(title)
    if feature_names is not None:
        ax.set_xlabel(feature_names[0])
        ax.set_ylabel(feature_names[1])
    else:
        ax.set_xlabel("x1")
        ax.set_ylabel("x2")

    ax.legend()
    ax.grid(True, alpha=0.25)

    if savepath is not None:
        plt.savefig(savepath, dpi=150, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close(fig)


def plot_clusters_2d(
    X: np.ndarray,
    labels: Sequence[int],
    title: str = "DBSCAN - Clusters",
    feature_names: Optional[Tuple[str, str]] = None,
    figsize: Tuple[int, int] = (7, 6),
    alpha: float = 0.85,
    s: int = 40,
    show: bool = True,
    savepath: Optional[str] = None,
) -> None:
    """
    Plota um scatter 2D colorindo por cluster (labels). Ruído (label=-1) aparece separado.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or X.shape[1] < 2:
        raise ValueError("X precisa ser 2D e ter pelo menos 2 colunas para plot 2D.")

    labels = _ensure_numpy_1d(labels, "labels")
    if labels.shape[0] != X.shape[0]:
        raise ValueError("labels deve ter o mesmo tamanho que X.")

    x0, x1 = X[:, 0], X[:, 1]

    fig = plt.figure(figsize=figsize)
    ax = plt.gca()

    unique = np.unique(labels)

    # Plota cada cluster com uma cor automática do matplotlib
    for lab in unique:
        mask = (labels == lab)
        if lab == -1:
            ax.scatter(x0[mask], x1[mask], label="Ruído (cluster=-1)", s=s, alpha=alpha, marker="x")
        else:
            ax.scatter(x0[mask], x1[mask], label=f"Cluster {lab}", s=s, alpha=alpha, marker="o")

    ax.set_title(title)
    if feature_names is not None:
        ax.set_xlabel(feature_names[0])
        ax.set_ylabel(feature_names[1])
    else:
        ax.set_xlabel("x1")
        ax.set_ylabel("x2")

    ax.legend()
    ax.grid(True, alpha=0.25)

    if savepath is not None:
        plt.savefig(savepath, dpi=150, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close(fig)


def plot_point_types_3d(
    X: np.ndarray,
    point_type: Sequence[PointType],
    dims: Tuple[int, int, int] = (0, 1, 2),
    title: str = "DBSCAN - Tipos de ponto (3D)",
    feature_names: Optional[Tuple[str, str, str]] = None,
    figsize: Tuple[int, int] = (8, 6),
    alpha: float = 0.85,
    s: int = 35,
    show: bool = True,
    savepath: Optional[str] = None,
) -> None:
    """
    Plota um scatter 3D escolhendo 3 dimensões de X (útil para Iris).
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or X.shape[1] < 3:
        raise ValueError("X precisa ser 2D e ter pelo menos 3 colunas para plot 3D.")

    pt = np.asarray(point_type, dtype=object)
    if pt.shape[0] != X.shape[0]:
        raise ValueError("point_type deve ter o mesmo tamanho que X.")

    d0, d1, d2 = dims
    if max(dims) >= X.shape[1] or min(dims) < 0:
        raise ValueError("dims inválido para o número de colunas de X.")

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection="3d")

    mask_core = (pt == "core")
    mask_border = (pt == "border")
    mask_noise = (pt == "noise")

    ax.scatter(X[mask_core, d0], X[mask_core, d1], X[mask_core, d2], label="Núcleo", s=s, alpha=alpha, marker="o")
    ax.scatter(X[mask_border, d0], X[mask_border, d1], X[mask_border, d2], label="Borda", s=s, alpha=alpha, marker="^")
    ax.scatter(X[mask_noise, d0], X[mask_noise, d1], X[mask_noise, d2], label="Ruído", s=s, alpha=alpha, marker="x")

    ax.set_title(title)
    if feature_names is not None:
        ax.set_xlabel(feature_names[0])
        ax.set_ylabel(feature_names[1])
        ax.set_zlabel(feature_names[2])
    else:
        ax.set_xlabel(f"x{d0}")
        ax.set_ylabel(f"x{d1}")
        ax.set_zlabel(f"x{d2}")

    ax.legend()
    if savepath is not None:
        plt.savefig(savepath, dpi=150, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close(fig)