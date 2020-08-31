from functools import reduce
def sum_equation(lista):
    x = reduce(lambda i,y:i+y, lista, 0)
    ListToStr = " ".join([str(elem) for elem in lista])
    y = ListToStr.split()
    if len(y) > 1:
        i = " + ".join(y) + " = " + str(x)
    else:
        i = "0 = " + str(x)
    return i


print(sum_equation([1,5,7]))


