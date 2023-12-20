def floyd_warshall(graph):
    V = list(graph.keys())
    n = len(V)

    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

        for nbr, wt in graph[V[i]]:
            dist[i][V.index(nbr)] = wt

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example graph represented as an adjacency list
G = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 5)],
    'C': [('A', 4), ('B', 1), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

# Run Floyd-Warshall algorithm
result = floyd_warshall(G)

# Display the result
print("Shortest path matrix:")
for row in result:
    print(row)
