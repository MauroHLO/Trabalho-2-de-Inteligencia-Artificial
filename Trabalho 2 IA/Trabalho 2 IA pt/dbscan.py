import numpy as np
from distances import distancia_entre_pares

def dbscan(X, eps, min_samples, metrica="euclideano"):
    X = np.asarray(X, dtype=float)
    n = X.shape[0]
    if n == 0:
        return np.array([]), np.array([])

    # Calcula distâncias
    dist = distancia_entre_pares(X, metrica)

    # Vizinhos: pontos <= eps (inclui self)
    vizinhos = [np.where(dist[i] <= eps)[0] for i in range(n)]
    contagem_vizinhos = np.array([len(nb) for nb in vizinhos])

    # Núcleos: >= min_samples
    vira_nucleo = contagem_vizinhos >= min_samples

    # Inicializações
    labels = np.full(n, -1)  # -1: ruído
    tipo_ponto = np.full(n, "ruido", dtype=object)
    cluster_id = 0
    visitado = np.zeros(n, dtype=bool)

    for i in range(n):
        if visitado[i]:
            continue
        visitado[i] = True

        if not vira_nucleo[i]:
            continue  # Ruído inicial

        # Novo cluster
        labels[i] = cluster_id
        tipo_ponto[i] = "nucleo"

        # Expansão (BFS)
        fila = list(vizinhos[i])
        while fila:
            j = fila.pop(0)
            if not visitado[j]:
                visitado[j] = True
                if vira_nucleo[j]:
                    fila.extend(vizinhos[j])

            if labels[j] == -1:
                labels[j] = cluster_id
                tipo_ponto[j] = "nucleo" if vira_nucleo[j] else "borda"

        cluster_id += 1

    # Consistência final
    tipo_ponto[(labels != -1) & (~vira_nucleo)] = "borda"
    tipo_ponto[labels == -1] = "ruido"

    return labels, tipo_ponto