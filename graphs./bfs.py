from collections import deque

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


