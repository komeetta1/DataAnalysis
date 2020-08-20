
def triple(triplattava):
    y = 0
    y += triplattava*3
    return y
def square(neliö):
    i = 0
    i += neliö**2
    return i

Lista = [1,2,3,4,5,6,7,8,9,10]

for i in Lista:
    if triple(i) <= square(i):
        break
    else:
        print(f"triple({i}) ==",triple(i), f"square({i}) ==",square(i))


