# main.py
from __future__ import annotations

import numpy as np

from datasets import get_two_moons, get_two_circles, get_iris
from dbscan import dbscan
from plots import (
    plot_point_types_2d,
    plot_clusters_2d,
    plot_point_types_3d,
)


def run_two_moons():
    data = get_two_moons(n_samples=600, noise=0.06, random_state=42)
    X = data.X

    # Você pode variar eps/min_samples e métricas aqui
    configs = [
        ("euclidean", 0.18, 6),
        ("manhattan", 0.25, 6),
        ("chebyshev", 0.12, 6),
    ]

    for metric, eps, min_samples in configs:
        res = dbscan(X, eps=eps, min_samples=min_samples, metric=metric)
        title = f"Two Moons | metric={metric} | eps={eps} | min_samples={min_samples}"

        plot_point_types_2d(
            X, res.point_type,
            title=title + " (core/border/noise)"
        )
        plot_clusters_2d(
            X, res.labels,
            title=title + " (clusters)"
        )


def run_two_circles():
    data = get_two_circles(n_samples=700, noise=0.05, factor=0.5, random_state=42)
    X = data.X

    configs = [
        ("euclidean", 0.18, 6),
        ("manhattan", 0.25, 6),
        ("chebyshev", 0.10, 6),
    ]

    for metric, eps, min_samples in configs:
        res = dbscan(X, eps=eps, min_samples=min_samples, metric=metric)
        title = f"Two Circles | metric={metric} | eps={eps} | min_samples={min_samples}"

        plot_point_types_2d(
            X, res.point_type,
            title=title + " (core/border/noise)"
        )
        plot_clusters_2d(
            X, res.labels,
            title=title + " (clusters)"
        )


def run_iris():
    data = get_iris()
    X = data.X
    y = data.y
    feat = data.feature_names
    targets = data.target_names

    # Enunciado sugere usar Euclidiana na Iris
    metric = "euclidean"

    # DBSCAN na Iris costuma precisar de eps relativamente pequeno,
    # depende da escala (em cm) e da escolha de dimensões.
    # Aqui vamos testar uns combos.
    configs = [
        (0.35, 5),
        (0.45, 5),
        (0.55, 5),
        (0.60, 5),
    ]

    # Plots com 2 variáveis (ex: petal length vs petal width -> colunas 2 e 3)
    d2 = (2, 3)
    X2 = X[:, d2]

    for eps, min_samples in configs:
        res2 = dbscan(X2, eps=eps, min_samples=min_samples, metric=metric)
        title = f"Iris(2D) | dims={d2} | eps={eps} | min_samples={min_samples}"

        plot_point_types_2d(
            X2,
            res2.point_type,
            title=title + " (core/border/noise)",
            feature_names=(feat[d2[0]], feat[d2[1]])
        )
        plot_clusters_2d(
            X2,
            res2.labels,
            title=title + " (clusters)",
            feature_names=(feat[d2[0]], feat[d2[1]])
        )

        # Dica para relatório: uma visão rápida do "ruído"
        noise_count = int(np.sum(res2.labels == -1))
        clusters_found = int(len(set(res2.labels)) - (1 if -1 in set(res2.labels) else 0))
        print(f"[IRIS 2D] eps={eps}, min_samples={min_samples} -> clusters={clusters_found}, ruido={noise_count}/150")

    # (Opcional) 3D com 3 variáveis (0,2,3) costuma separar bem visualmente
    d3 = (0, 2, 3)
    X3 = X[:, d3]

    eps_3d, min_samples_3d = 0.55, 5
    res3 = dbscan(X3, eps=eps_3d, min_samples=min_samples_3d, metric=metric)

    plot_point_types_3d(
        X3,
        res3.point_type,
        dims=(0, 1, 2),
        title=f"Iris(3D) | dims={d3} | eps={eps_3d} | min_samples={min_samples_3d}",
        feature_names=(feat[d3[0]], feat[d3[1]], feat[d3[2]]),
    )

    # Observação útil pro relatório: comparação rápida com classes reais
    # (Não é "acurácia", é só uma inspeção: cada cluster tende a agrupar uma espécie?)
    print("\n[IRIS] Distribuição de espécies por cluster (usando dims 3D escolhidas):")
    labels = res3.labels
    unique_labels = sorted(set(labels))
    for lab in unique_labels:
        mask = (labels == lab)
        if lab == -1:
            name = "Ruído (-1)"
        else:
            name = f"Cluster {lab}"

        if y is not None:
            counts = np.bincount(y[mask], minlength=len(targets))
            counts_str = ", ".join([f"{targets[i]}={counts[i]}" for i in range(len(targets))])
            print(f"  {name}: {counts_str} | total={int(np.sum(mask))}")


def main():
    # Rode um por vez, ou deixe todos ligados.
    run_two_moons()
    run_two_circles()
    run_iris()


if __name__ == "__main__":
    main()