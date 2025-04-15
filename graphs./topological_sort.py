def topological_sort(graph):
    n = len(graph)
    result = []
    visited = [False] * n

    def dfs_visit(v):
        nonlocal result
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u)

#when we procced vertex we append it, at the end we reverse the list, we could also appendleft and dont reverse 
        result.append(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return reversed(result)
