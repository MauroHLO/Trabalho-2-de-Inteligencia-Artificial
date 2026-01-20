import numpy as np
from distances import pairwise_distances

def dbscan(X, eps, min_samples, metric="euclidean"):
    X = np.asarray(X, dtype=float)
    n = X.shape[0]
    if n == 0:
        return np.array([]), np.array([])

    # Calcula distâncias
    dist = pairwise_distances(X, metric)

    # Vizinhos: pontos <= eps (inclui self)
    neighbors = [np.where(dist[i] <= eps)[0] for i in range(n)]
    neighbor_counts = np.array([len(nb) for nb in neighbors])

    # Núcleos: >= min_samples
    is_core = neighbor_counts >= min_samples

    # Inicializações
    labels = np.full(n, -1)  # -1: ruído
    point_type = np.full(n, "noise", dtype=object)
    cluster_id = 0
    visited = np.zeros(n, dtype=bool)

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True

        if not is_core[i]:
            continue  # Ruído inicial

        # Novo cluster
        labels[i] = cluster_id
        point_type[i] = "core"

        # Expansão (BFS)
        queue = list(neighbors[i])
        while queue:
            j = queue.pop(0)
            if not visited[j]:
                visited[j] = True
                if is_core[j]:
                    queue.extend(neighbors[j])

            if labels[j] == -1:
                labels[j] = cluster_id
                point_type[j] = "core" if is_core[j] else "border"

        cluster_id += 1

    # Consistência final
    point_type[(labels != -1) & (~is_core)] = "border"
    point_type[labels == -1] = "noise"

    return labels, point_type