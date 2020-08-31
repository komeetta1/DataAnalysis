

def positive_list(Lista):
    posList = list(filter(lambda x : x > 0, Lista))
    return posList

print(positive_list([2,-2,0,1,-7]))