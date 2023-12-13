def tsp(graph):
    n = len(graph)
    all_vertices = (1 << n) - 1

    D = [[float('inf')] * n for _ in range(2 ** n)]
    P = [[None] * n for _ in range(2 ** n)]

    for v in range(n):
        D[2 ** v][v] = graph[0][v]

    for subset in range(1, (2 ** n)):
        for v in range(n):
            if (subset and (2 ** v)) != 0:
                for u in range(n):
                    if (subset and (2 ** u)) != 0 and u != v:
                        if D[subset][v] > D[subset ^ (2 ** v)][u] + graph[u][v]:
                            D[subset][v] = D[subset ^ (2 ** v)][u] + graph[u][v]
                            P[subset][v] = u

    subset = all_vertices
    last_vertex = 0
    optimal_path = [None] * (n + 1)
    optimal_path[0] = last_vertex

    for i in range(n - 1, 0, -1):
        prev_vertex = P[subset][last_vertex]
        optimal_path[i] = prev_vertex
        subset ^= (1 << last_vertex)
        last_vertex = prev_vertex

    optimal_path[-1] = 0
    optimal_path.reverse()
    return optimal_path


graph = [
    [0, 4, 1, 3],
    [4, 0, 2, 1],
    [1, 2, 0, 5],
    [3, 1, 5, 0]
]

optimal_path = tsp(graph)
print("Optimal Path: ", optimal_path)
