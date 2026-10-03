INF = float("inf")


def floyd_warshall(graph):
    n = len(graph)
    # копия
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_matrix(m):
    for row in m:
        print("  " + " ".join(f"{x:>4}" if x != INF else " INF" for x in row))