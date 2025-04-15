#shortes path with w>=0
import heapq
#for matrix rep. O(V^2)

def dijkstra(G,s):#O(ElogV) dla grafow rzadkich V~E, ale generalnie O((V+E)logV)
    n=len(G)
    d=[float('inf') for i in range(n)]
    parent=[None for i in range(n)]
    d[s]=0  

    Q=[]
    heapq.heappush(Q,(d[s],s))

    while Q:
        dist,u = heapq.heappop(Q)

        if dist > d[u]:
            continue

        for v,weight in G[u]:
            if d[v]>d[u]+weight:
                d[v] = d[u]+weight
                parent[v]=u 
                heapq.heappush(Q,(d[v],v))

    return d 
  
G2 = [
    [(1, 10), (2, 1)],   # 0
    [(3, 1)],            # 1
    [(1, 1)],            # 2
    []                   # 3
]


print(dijkstra(G2,0))
