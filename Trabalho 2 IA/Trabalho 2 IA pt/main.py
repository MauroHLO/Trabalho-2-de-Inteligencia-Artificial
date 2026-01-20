import numpy as np
from datasets import get_duas_luas, get_dois_circulos, get_iris
from dbscan import dbscan
from plots import plot_tipos_pontos_2d, plot_clusters, plot_tipos_pontos_3d

def rodar_duas_luas():
    X, y, feat, targets = get_duas_luas(n_samples=600, noise=0.06, random_state=42)
    configs = [("euclidiano", 0.18, 6), ("manhattan", 0.25, 6), ("chebyshev", 0.12, 6)]

    for metrica, eps, min_samples in configs:
        labels, tipos_pontos = dbscan(X, eps, min_samples, metrica)
        titulo = f"Duas Luas | {metrica} | eps={eps} | min_samples={min_samples}"
        plot_tipos_pontos_2d(X, tipos_pontos, titulo + " (tipos)", feat)
        plot_clusters(X, labels, titulo + " (clusters)", feat)

def rodar_dois_circulos():
    X, y, feat, targets = get_dois_circulos(n_samples=700, noise=0.05, random_state=42)
    configs = [("euclidiano", 0.18, 6), ("manhattan", 0.25, 6), ("chebyshev", 0.10, 6)]

    for metrica, eps, min_samples in configs:
        labels, tipos_pontos = dbscan(X, eps, min_samples, metrica)
        titulo = f"Two Circles | {metrica} | eps={eps} | min_samples={min_samples}"
        plot_tipos_pontos_2d(X, tipos_pontos, titulo + " (tipos)", feat)
        plot_clusters(X, labels, titulo + " (clusters)", feat)

def rodar_iris():
    X, y, feat, targets = get_iris()
    metrica = "euclidiano"
    configs = [(0.35, 5), (0.45, 5), (0.55, 5), (0.60, 5)]

    d2 = (2, 3)
    X2 = X[:, d2]
    for eps, min_samples in configs:
        labels, tipos_pontos = dbscan(X2, eps, min_samples, metrica)
        titulo = f"Iris(2D) | dims={d2} | eps={eps} | min_samples={min_samples}"
        plot_tipos_pontos_2d(X2, tipos_pontos, titulo + " (tipos)", (feat[d2[0]], feat[d2[1]]))
        plot_clusters(X2, labels, titulo + " (clusters)", (feat[d2[0]], feat[d2[1]]))

        contador_ruido = np.sum(labels == -1)
        clusters_encontrados = len(set(labels)) - (1 if -1 in labels else 0)
        print(f"[IRIS 2D] eps={eps}, min_samples={min_samples} -> clusters={clusters_encontrados}, ruido={contador_ruido}/150")

    # 3D: cols 0,2,3
    d3 = (0, 2, 3)
    X3 = X[:, d3]
    eps, min_samples = 0.55, 5
    labels, tipos_pontos = dbscan(X3, eps, min_samples, metrica)
    plot_tipos_pontos_3d(X3, tipos_pontos, dims=(0, 1, 2), titulo=f"Iris(3D) | dims={d3} | eps={eps} | min_samples={min_samples}", nome_feature=(feat[d3[0]], feat[d3[1]], feat[d3[2]]))

    print("\n[IRIS 3D] Distribuição de espécies por cluster:")
    unique_labels = np.unique(labels)
    for lab in unique_labels:
        mask = (labels == lab)
        name = "Ruído" if lab == -1 else f"Cluster {lab}"
        counts = np.bincount(y[mask], minlength=len(targets))
        counts_str = ", ".join([f"{targets[i]}={counts[i]}" for i in range(len(targets))])
        print(f"  {name}: {counts_str} | total={np.sum(mask)}")



def main():
    rodar_duas_luas()
    rodar_dois_circulos()
    rodar_iris()

if __name__ == "__main__":
    main()