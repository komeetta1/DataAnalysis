
d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}


def reverse_dictionary(dictio):
    reverse = {}
    for k,v in dictio.items():
        for x in v:
            reverse.setdefault(x,[]).append(k)
    return reverse

print(reverse_dictionary(d))