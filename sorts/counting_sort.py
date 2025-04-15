def counting_sort(T, k):
    n=len(T)
    B=[0]*n
    C=[0]*k
    for i in range(n):
        C[T[i]]+=1
    for i in range(1, k):
        C[i]+=C[i-1]
    for i in range(n-1, -1, -1):
        B[C[T[i]]-1]=T[i]
        C[T[i]]-=1
    for i in range(n):
        T[i]=B[i]
    return T

def counting_sort_v2(T):
    n=len(T)
    max_val=max(T)
    min_val=min(T)
    k=max_val-min_val+1
    B=[0]*n
    C=[0]*k
    for i in range(n):
        C[T[i]-min_val]+=1
    for i in range(1, k):
        C[i]+=C[i-1]
    for i in range(n-1, -1, -1):
        B[C[T[i]-min_val]-1]=T[i]
        C[T[i]-min_val]-=1
    for i in range(n):
        T[i]=B[i]
    return T
