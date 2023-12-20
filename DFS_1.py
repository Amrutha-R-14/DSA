import networkx as nx
import matplotlib.pyplot as plt

def make_graph():
    return {
        'A': ['F', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['B', 'F'],
        'D': ['A', 'F'],
        'E': ['C', 'F'],
        'F': ['B', 'D', 'E'],
    }

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

def plot_graph(graph, title):
    G = nx.Graph()
    for node, neighbors in graph.items():
        G.add_edges_from((node, neighbor) for neighbor in neighbors)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')

    plt.title(title)
    plt.show()

def main():
    G = make_graph()

    plot_graph(G, "Original Graph")

    start_node = 'D'
    print(f"DFS starting from node {start_node}:")
    dfs(G, start_node, set())

if __name__ == "__main__":
    main()
