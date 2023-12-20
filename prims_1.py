import heapq
import networkx as nx
import matplotlib.pyplot as plt

def make_graph():
    return {
        'A': [('D', 3), ('C', 3), ('B', 2)],
        'B': [('A', 2), ('C', 4), ('E', 3)],
        'C': [('A', 3), ('D', 5), ('F', 6), ('E', 1), ('B', 4)],
        'D': [('A', 3), ('C', 5), ('F', 7)],
        'E': [('F', 8), ('C', 1), ('B', 3)],
        'F': [('G', 9), ('E', 8), ('C', 6), ('D', 7)],
        'G': [('F', 9)],
    }

def prims(G, start='A'):
    unvisited = list(G.keys())
    visited = []
    total_cost = 0
    MST = []

    unvisited.remove(start)
    visited.append(start)

    heap = [(cost, start, node) for node, cost in G[start]]
    heapq.heapify(heap)

    while unvisited:
        cost, n1, n2 = heapq.heappop(heap)
        new_node = None

        if n1 in unvisited and n2 in visited:
            new_node = n1
            MST.append((n2, n1, cost))

        elif n1 in visited and n2 in unvisited:
            new_node = n2
            MST.append((n1, n2, cost))

        if new_node is not None:
            unvisited.remove(new_node)
            visited.append(new_node)
            total_cost += cost

            for node, c in G[new_node]:
                heapq.heappush(heap, (c, new_node, node))

    return MST, total_cost

def plot_graph_with_mst(graph, mst_edges, title):
    G = nx.Graph()
    for node, edges in graph.items():
        G.add_edges_from((node, v, {'weight': w}) for v, w in edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): str(d['weight']) for u, v, d in G.edges(data=True)})
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r', width=2)

    plt.title(title)
    plt.show()

def main():
    G = make_graph()
    MST, total_cost = prims(G, 'A')

    print(f'Minimum spanning tree: {MST}')
    print(f'Total cost: {total_cost}')

    plot_graph_with_mst(G, MST, "Graph with Minimum Spanning Tree")

main()
