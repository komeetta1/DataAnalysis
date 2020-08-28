

def transform(lista,lista2):
    '''
    L1 = lista.split()
    L1 = [int(i) for i in L1]
    '''
    L1 = lista.split()
    L1int = list(map(int, L1))
    L2 = lista2.split()
    L2int = list(map(int, L2))
    y = [k * j for k, j in zip(L1int, L2int)]
    return y
print(transform("1 5 3", "2 6 -1"))