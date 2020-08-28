lists_of_lists = [[1, 2, 3], [4, 5, 6]]
y = [sum(x) for x in zip(*lists_of_lists)]
print(y)