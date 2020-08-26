
L1 = [1, 2, 3]
L2 = [10, 20, 10]
L3 = ["first", "second", "third"]


def interleave(Lista1, Lista2, Lista3):
    zip_list = list(zip(Lista1, Lista2, Lista3))
    return zip_list


print(interleave(L1, L2, L3))
