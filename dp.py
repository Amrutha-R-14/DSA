from collections import defaultdict

def longest_path_dag(graph, start, memo={}):
    if start in memo:
        return memo[start]

    if not graph[start]:
        result = 0
    else:
        result = max([1 + longest_path_dag(graph, neighbor, memo) for neighbor in graph[start]])

    memo[start] = result
    return result

# Example usage
dag = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

start_node = 'A'
result = longest_path_dag(dag, start_node)
print(f"The length of the longest path starting from {start_node} is: {result}")
