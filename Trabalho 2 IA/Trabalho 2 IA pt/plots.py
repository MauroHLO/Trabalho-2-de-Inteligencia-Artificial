import numpy as np
import matplotlib.pyplot as plt

def plot_tipos_pontos_2d(X, tipo_ponto, titulo="DBSCAN - Tipos de ponto", nome_feature=None, tamanho_fig=(7, 6), show=True):
    X = np.asarray(X)

    x0, x1 = X[:, 0], X[:, 1]
    fig = plt.figure(figsize=tamanho_fig)
    ax = plt.gca()

    mask_nucleo = (tipo_ponto == "nucleo")
    mask_borda = (tipo_ponto == "borda")
    mask_ruido = (tipo_ponto == "ruido")

    ax.scatter(x0[mask_nucleo], x1[mask_nucleo], label="Núcleo", marker="o")
    ax.scatter(x0[mask_borda], x1[mask_borda], label="Borda", marker="^")
    ax.scatter(x0[mask_ruido], x1[mask_ruido], label="Ruído", marker="x")

    ax.set_title(titulo)
    ax.set_xlabel(nome_feature[0] if nome_feature else "x1")
    ax.set_ylabel(nome_feature[1] if nome_feature else "x2")
    ax.legend()
    ax.grid(True)

    if show:
        plt.show()
    else:
        plt.close(fig)


def plot_clusters(X, labels, titulo="DBSCAN - Clusters", nome_feature=None, tamanho_fig=(7, 6), show=True):
    X = np.asarray(X)

    x0, x1 = X[:, 0], X[:, 1]
    fig = plt.figure(figsize=tamanho_fig)
    ax = plt.gca()

    unique = np.unique(labels)
    for lab in unique:
        mask = (labels == lab)
        if lab == -1:
            ax.scatter(x0[mask], x1[mask], label="Ruído", marker="x")
        else:
            ax.scatter(x0[mask], x1[mask], label=f"Cluster {lab}", marker="o")

    ax.set_title(titulo)
    ax.set_xlabel(nome_feature[0] if nome_feature else "x1")
    ax.set_ylabel(nome_feature[1] if nome_feature else "x2")
    ax.legend()
    ax.grid(True)

    if show:
        plt.show()
    else:
        plt.close(fig)

def plot_tipos_pontos_3d(X, tipos_pontos, dims=(0, 1, 2), titulo="DBSCAN - Tipos de ponto (3D)", nome_feature=None, tamanho_fig=(8, 6), show=True):
    X = np.asarray(X)

    d0, d1, d2 = dims
    fig = plt.figure(figsize=tamanho_fig)
    ax = fig.add_subplot(111, projection="3d")

    mask_nucleo = (tipos_pontos == "nucleo")
    mask_borda = (tipos_pontos == "borda")
    mask_ruido = (tipos_pontos == "ruido")

    ax.scatter(X[mask_nucleo, d0], X[mask_nucleo, d1], X[mask_nucleo, d2], label="Núcleo", marker="o")
    ax.scatter(X[mask_borda, d0], X[mask_borda, d1], X[mask_borda, d2], label="Borda", marker="^")
    ax.scatter(X[mask_ruido, d0], X[mask_ruido, d1], X[mask_ruido, d2], label="Ruído", marker="x")

    ax.set_title(titulo)
    ax.set_xlabel(nome_feature[0] if nome_feature else f"x{d0}")
    ax.set_ylabel(nome_feature[1] if nome_feature else f"x{d1}")
    ax.set_zlabel(nome_feature[2] if nome_feature else f"x{d2}")
    ax.legend()

    if show:
        plt.show()
    else:
        plt.close(fig)

