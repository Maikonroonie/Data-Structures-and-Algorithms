#shortest paths with any w

def bellman_ford(G,s):#O(V*E)
    n=len(G)
    d=[float('inf') for i in range(n)]
    d[s]=0 

    for i in range(n-1): #najdłuższa mozliwa ścieżka w grafie bez cykli zawiera co najwyżej n-1 krawędzi
        for node in G:
            for nb, weight in G[node]:    #relaksacja każdej krawędzi w grafie (razem n-1 razy) i potem jeszcze raz zeby wykryc potencjlany ujemny cykl
                if d[node] != float('inf') and d[nb] > d[node] + weight:
                    d[nb] = d[node] + weight 


    for node in G:#wykrywanie cyku z ujemną wagą
            for nb, weight in G[node]: 
                if d[node] != float('inf') and d[nb] > d[node] + weight:
                    print("negative weight cycle")
                    return None

    return d
