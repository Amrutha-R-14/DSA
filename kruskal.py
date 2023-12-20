import networkx as nx
import matplotlib.pyplot as plt

def kruskal(graph):
    # Sort all the edges in non-decreasing order of their weight
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])

    # Initialize a disjoint set data structure
    parent = {node: node for node in graph.nodes}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        parent[root1] = root2

    # Initialize the minimum spanning tree
    mst = nx.Graph()

    for edge in edges:
        node1, node2, weight = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.add_edge(node1, node2, weight=weight['weight'])

    return mst

def plot_graph(graph, title):
    pos = nx.circular_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Create a cyclic graph (ring)
    G = nx.cycle_graph(5)
    for edge in G.edges():
        G[edge[0]][edge[1]]['weight'] = 1  # Assign weights for simplicity

    # Run Kruskal's algorithm
    mst = kruskal(G)

    # Plot the original graph and the minimum spanning tree
    plot_graph(G, "Original Graph")
    plot_graph(mst, "Minimum Spanning Tree")
