#depth first search
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack= [start]
    visited.add(start)
    while stack:
        node = stack.pop()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
def dfs_matrix(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        node = stack.pop()
        print(node)
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
#depth first search
graph_matrix=[[0,1,1,0],
              [1,0,0,1],
              [1,0,0,1],
              [0,1,1,0]]
graph=[[1,2],[0,3],[0,3],[1,2]]
dfs_recursive(graph,0)
dfs_iterative(graph,0)
dfs_matrix(graph_matrix,0)
