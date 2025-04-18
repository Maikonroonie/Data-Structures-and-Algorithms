from collections import deque


def has_cycle(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent=[None for _ in range(n)]

    for start in range(n):
        if not visited[start]:
            queue=deque()
            queue.append(start)
            visited[start]=True

            while queue:
                v = queue.popleft()

                for u in graph[v]:
                    if not visited[u]:
                        parent[u]=v
                        visited[u] = True
                        queue.append(u)
                    elif parent[v]!=u:
                        return True

    return False

graph = [
    [1],    # 0
    [0, 2], # 1
    [1]     # 2
]
print(has_cycle(graph))
