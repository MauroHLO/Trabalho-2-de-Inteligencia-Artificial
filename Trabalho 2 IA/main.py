import numpy as np
from datasets import get_two_moons, get_two_circles, get_iris
from dbscan import dbscan
from plots import plot_point_types_2d, plot_clusters_2d, plot_point_types_3d

def run_two_moons():
    X, y, feat, targets = get_two_moons(n_samples=600, noise=0.06, random_state=42)
    configs = [("euclidean", 0.18, 6), ("manhattan", 0.25, 6), ("chebyshev", 0.12, 6)]

    for metric, eps, min_samples in configs:
        labels, point_type = dbscan(X, eps, min_samples, metric)
        title = f"Two Moons | {metric} | eps={eps} | min_samples={min_samples}"
        plot_point_types_2d(X, point_type, title + " (tipos)", feat)
        plot_clusters_2d(X, labels, title + " (clusters)", feat)

def run_two_circles():
    X, y, feat, targets = get_two_circles(n_samples=700, noise=0.05, random_state=42)
    configs = [("euclidean", 0.18, 6), ("manhattan", 0.25, 6), ("chebyshev", 0.10, 6)]

    for metric, eps, min_samples in configs:
        labels, point_type = dbscan(X, eps, min_samples, metric)
        title = f"Two Circles | {metric} | eps={eps} | min_samples={min_samples}"
        plot_point_types_2d(X, point_type, title + " (tipos)", feat)
        plot_clusters_2d(X, labels, title + " (clusters)", feat)

def run_iris():
    X, y, feat, targets = get_iris()
    metric = "euclidean"
    configs = [(0.35, 5), (0.45, 5), (0.55, 5), (0.60, 5)]

    # 2D: cols 2 e 3
    d2 = (2, 3)
    X2 = X[:, d2]
    for eps, min_samples in configs:
        labels, point_type = dbscan(X2, eps, min_samples, metric)
        title = f"Iris(2D) | dims={d2} | eps={eps} | min_samples={min_samples}"
        plot_point_types_2d(X2, point_type, title + " (tipos)", (feat[d2[0]], feat[d2[1]]))
        plot_clusters_2d(X2, labels, title + " (clusters)", (feat[d2[0]], feat[d2[1]]))

        noise_count = np.sum(labels == -1)
        clusters_found = len(set(labels)) - (1 if -1 in labels else 0)
        print(f"[IRIS 2D] eps={eps}, min_samples={min_samples} -> clusters={clusters_found}, ruido={noise_count}/150")

    # 3D: cols 0,2,3
    d3 = (0, 2, 3)
    X3 = X[:, d3]
    eps, min_samples = 0.55, 5
    labels, point_type = dbscan(X3, eps, min_samples, metric)
    plot_point_types_3d(X3, point_type, dims=(0,1,2), title=f"Iris(3D) | dims={d3} | eps={eps} | min_samples={min_samples}", feature_names=(feat[d3[0]], feat[d3[1]], feat[d3[2]]))

    print("\n[IRIS 3D] Distribuição de espécies por cluster:")
    unique_labels = np.unique(labels)
    for lab in unique_labels:
        mask = (labels == lab)
        name = "Ruído" if lab == -1 else f"Cluster {lab}"
        counts = np.bincount(y[mask], minlength=len(targets))
        counts_str = ", ".join([f"{targets[i]}={counts[i]}" for i in range(len(targets))])
        print(f"  {name}: {counts_str} | total={np.sum(mask)}")

def main():
    run_two_moons()
    run_two_circles()
    run_iris()

if __name__ == "__main__":
    main()