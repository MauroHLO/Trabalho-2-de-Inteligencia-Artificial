# datasets.py
from __future__ import annotations

import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple

from sklearn.datasets import make_moons, make_circles, load_iris


@dataclass
class DatasetBundle:
    """
    Estrutura padrão para retornar datasets de forma consistente.
    - X: (N, D) features
    - y: (N,) labels reais (None quando não existir)
    - feature_names: nomes das features (None quando não aplicável)
    - target_names: nomes das classes (None quando não aplicável)
    """
    X: np.ndarray
    y: Optional[np.ndarray]
    feature_names: Optional[list[str]] = None
    target_names: Optional[list[str]] = None


def get_two_moons(
    n_samples: int = 500,
    noise: float = 0.05,
    random_state: int = 42,
) -> DatasetBundle:
    """
    Gera a base Two Moons.
    """
    X, y = make_moons(n_samples=n_samples, noise=noise, random_state=random_state)
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=int)
    return DatasetBundle(
        X=X,
        y=y,
        feature_names=["x1", "x2"],
        target_names=["moon_0", "moon_1"],
    )


def get_two_circles(
    n_samples: int = 500,
    noise: float = 0.05,
    factor: float = 0.5,
    random_state: int = 42,
) -> DatasetBundle:
    """
    Gera a base Two Circles.
    factor: escala do círculo interno (0 < factor < 1)
    """
    X, y = make_circles(
        n_samples=n_samples, noise=noise, factor=factor, random_state=random_state
    )
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=int)
    return DatasetBundle(
        X=X,
        y=y,
        feature_names=["x1", "x2"],
        target_names=["circle_outer", "circle_inner"],
    )


def get_iris() -> DatasetBundle:
    """
    Carrega a base Iris (sklearn).
    """
    iris = load_iris()
    X = np.asarray(iris.data, dtype=float)      # (150, 4)
    y = np.asarray(iris.target, dtype=int)      # (150,)
    feature_names = list(iris.feature_names)    # ex: 'sepal length (cm)'...
    target_names = list(iris.target_names)      # ['setosa', 'versicolor', 'virginica']
    return DatasetBundle(
        X=X,
        y=y,
        feature_names=feature_names,
        target_names=target_names,
    )