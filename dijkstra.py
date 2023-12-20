import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    pred = {node: None for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > dist[cur_node]:
            continue

        for n, we in graph[cur_node]:
            dis = cur_dist + we

            if dis < dist[n]:
                dist[n] = dis
                pred[n] = cur_node
                heapq.heappush(pq, (dis, n))

    return dist, pred

def print_shortest_path(pred, dest):
    path = []
    cur_node = dest

    while cur_node is not None:
        path.insert(0, cur_node)
        cur_node = pred[cur_node]

    print(f"Shortest path to {dest}: {' -> '.join(path)}")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}


start = 'A'


distances, predecessors = dijkstra(graph, start)


for node in graph:
    print(f"Distance to {node}: {distances[node]}")
    print_shortest_path(predecessors, node)
    print()
