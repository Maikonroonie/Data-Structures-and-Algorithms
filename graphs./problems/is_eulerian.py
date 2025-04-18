def is_connected(graph):
    n = len(graph)
    visited = [False] * n

    def dfs_visit(v):
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u)

    dfs_visit(0)

    for v in range(n):
        # If vertex wasn't visited, and it
        # is not isolated.
        if not visited[v] and len(graph[v]):
            return False

    return True


def is_eulerian_connected(graph):
    n = len(graph)

    if not is_connected(graph):
        return False

    for v in range(n):
        if len(graph[v]) % 2 == 1:
            return False

    return True
