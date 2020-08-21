
L1 = [1,6,4,5,8,1]
L2 = [6,4,7,2,8,3]

def merge(Lista1, Lista2):
    L = Lista1 + Lista2
    return L

print(sorted(merge(L1, L2)))
