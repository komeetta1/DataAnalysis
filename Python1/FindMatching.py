#return the indices to those elements in the input list that contain the search string.

def find_matching(lista, etsittävä):
    i = []
    for count,elem in enumerate(lista):
        if etsittävä in elem:
            i.append(count)
    return i
print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))