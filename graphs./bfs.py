from math import inf
from collections import deque

def dfs_list(graph):
    n = len(graph)

    time = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    discovery = [inf for _ in range(n)]
    processed = [inf for _ in range(n)]

    def dfs_visit(v):
        nonlocal time

        # Increment time at visit
        time += 1
        discovery[v] = time
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                dfs_visit(u)

        # Increment time at backtrack
        time += 1
        processed[v] = time

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return visited, parent, discovery, processed


def dfs_matrix(graph):
    n = len(graph)

    time = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    discovery = [inf for _ in range(n)]
    processed = [inf for _ in range(n)]

    def dfs_visit(v):
        nonlocal time

        # Increment time at visit
        time += 1
        visited[v] = True
        discovery[v] = time

        for u in range(n):
            if graph[v][u] == 1 and not visited[u]:
                parent[u] = v
                dfs_visit(u)

        # Increment time at backtrack
        time += 1
        processed[v] = time

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return visited, parent, discovery, processed


def bfs_list(graph, s):
    n = len(graph)
    queue = deque()

    # Initialize state arrays.
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]

    # Mark starting node as visited.
    visited[s] = True
    distance[s] = 0
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        # For every neighbour of v.
        for u in graph[v]:
            # Skip it if it's already visited.
            if visited[u]:
                continue

            # Mark it as visited.
            visited[u] = True
            parent[u] = v
            distance[u] = distance[v] + 1
            queue.appendleft(u)

    return visited, distance, parent


def bfs_matrix(graph, s):
    n = len(graph)
    queue = deque()

    # Initialize state arrays.
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]

    # Mark starting node as visited.
    visited[s] = True
    distance[s] = 0
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        # This for always makes O(V) iterations
        # making the algorithm run in O(V^2)
        # time regardless of graph's density.
        for u in range(n):
            if graph[v][u] != 1 or visited[u]:
                continue

            visited[u] = True
            parent[u] = v
            distance[u] = distance[v] + 1
            queue.appendleft(u)

    return visited, distance, parent



#bfs (breadth first search)
def bfs_iterative(graph, start):
    visited=set()
    q=deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


def bfs_matrix(graph, start):
    visited=set()
    q=deque([start])
    visited.add(start)
    while q:
        node=q.popleft()
        print(node)
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


graph_matrix=[[0,1,1,0],
              [1,0,0,1],
              [1,0,0,1],
              [0,1,1,0]]

graph=[[1,2],[0,3],[0,3],[1,2]]

bfs_iterative(graph,0)
bfs_recursive(graph, 0)
bfs_matrix(graph_matrix, 0)




def bfs(graph, s, visited=None):
    if visited==None:
        visited=set()
    q=deque([s])
    visited.add(s)
    while q:
        node=q.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


