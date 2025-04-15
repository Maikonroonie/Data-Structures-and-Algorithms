from collections import deque


def is_connected(graph):
    n = len(graph)

    queue = deque()
    visited = [False] * n

    # Process first node (arbitrary one)
    visits = 1
    visited[0] = True
    queue.append(0)

    while queue:
        v = queue.popleft()

        for u in graph[v]:
            if not visited[u]:
                visits += 1
                visited[u] = True
                queue.append(u)

    # If we have visited every node in the graph
    # number of visits should be equal to number of nodes.
    return visits == n
