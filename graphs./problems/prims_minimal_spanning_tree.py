import heapq

def prims_algorithm(graph, start):
    n=len(graph)
    Q=[]
    visited=[False for _ in range(n)]
    mst=[] # minimal spannig tree
    total_cost=0
    
    visited[start]=True
    for nb, weight in graph[start]:
        heapq.heappush(Q, (weight, start, nb))

    while Q:
        weight, u, v = heapq.heappop(Q)
        if not visited[v]:
            visited[v]=True
            mst.append((u, v))
            total_cost+=weight
            for nb, weight in graph[v]:
                if not visited[nb]:
                    heapq.heappush(Q, (weight, v, nb))
    return mst, total_cost

