import numpy as np
import matplotlib.pyplot as plt

def plot_point_types_2d(X, point_type, title="DBSCAN - Tipos de ponto", feature_names=None, figsize=(7, 6), show=True):
    X = np.asarray(X)
    if X.shape[1] < 2:
        raise ValueError("X precisa de pelo menos 2 colunas.")

    x0, x1 = X[:, 0], X[:, 1]
    fig = plt.figure(figsize=figsize)
    ax = plt.gca()

    mask_core = (point_type == "core")
    mask_border = (point_type == "border")
    mask_noise = (point_type == "noise")

    ax.scatter(x0[mask_core], x1[mask_core], label="Núcleo", marker="o")
    ax.scatter(x0[mask_border], x1[mask_border], label="Borda", marker="^")
    ax.scatter(x0[mask_noise], x1[mask_noise], label="Ruído", marker="x")

    ax.set_title(title)
    ax.set_xlabel(feature_names[0] if feature_names else "x1")
    ax.set_ylabel(feature_names[1] if feature_names else "x2")
    ax.legend()
    ax.grid(True)

    if show:
        plt.show()
    else:
        plt.close(fig)

def plot_clusters_2d(X, labels, title="DBSCAN - Clusters", feature_names=None, figsize=(7, 6), show=True):
    X = np.asarray(X)
    if X.shape[1] < 2:
        raise ValueError("X precisa de pelo menos 2 colunas.")

    x0, x1 = X[:, 0], X[:, 1]
    fig = plt.figure(figsize=figsize)
    ax = plt.gca()

    unique = np.unique(labels)
    for lab in unique:
        mask = (labels == lab)
        if lab == -1:
            ax.scatter(x0[mask], x1[mask], label="Ruído", marker="x")
        else:
            ax.scatter(x0[mask], x1[mask], label=f"Cluster {lab}", marker="o")

    ax.set_title(title)
    ax.set_xlabel(feature_names[0] if feature_names else "x1")
    ax.set_ylabel(feature_names[1] if feature_names else "x2")
    ax.legend()
    ax.grid(True)

    if show:
        plt.show()
    else:
        plt.close(fig)

def plot_point_types_3d(X, point_type, dims=(0, 1, 2), title="DBSCAN - Tipos de ponto (3D)", feature_names=None, figsize=(8, 6), show=True):
    X = np.asarray(X)
    if X.shape[1] < 3:
        raise ValueError("X precisa de pelo menos 3 colunas.")

    d0, d1, d2 = dims
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection="3d")

    mask_core = (point_type == "core")
    mask_border = (point_type == "border")
    mask_noise = (point_type == "noise")

    ax.scatter(X[mask_core, d0], X[mask_core, d1], X[mask_core, d2], label="Núcleo", marker="o")
    ax.scatter(X[mask_border, d0], X[mask_border, d1], X[mask_border, d2], label="Borda", marker="^")
    ax.scatter(X[mask_noise, d0], X[mask_noise, d1], X[mask_noise, d2], label="Ruído", marker="x")

    ax.set_title(title)
    ax.set_xlabel(feature_names[0] if feature_names else f"x{d0}")
    ax.set_ylabel(feature_names[1] if feature_names else f"x{d1}")
    ax.set_zlabel(feature_names[2] if feature_names else f"x{d2}")
    ax.legend()

    if show:
        plt.show()
    else:
        plt.close(fig)