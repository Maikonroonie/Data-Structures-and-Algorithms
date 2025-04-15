def merge(A, B): # funkcja merge "merguje" czyli jakby skala dwie tablice w posortowana jedna, pozniej jak bedzie wywolana w merge sorcie, to scala dwie czecsi lewa i prawa
    C=[]
    i=0
    j=0
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    while i<len(A):
        C.append(A[i])
        i+=1
    while j<len(B):
        C.append(B[j])
        j+=1
    return C
def merge_sort(T):
    if len(T)<=1:
        return T
    mid = len(T)//2
    left=merge_sort(T[:mid]) # od poczatku do polowy
    right=merge_sort(T[mid:]) # od polowy do konca
    return merge(left, right)
# merge sort to algorytm o zlozonosci nlogn dziala on czysto na rekurencji
