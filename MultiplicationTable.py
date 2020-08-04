for i in range(1, 11):
    print(end=" ")
    for x in range(1, 11):
        print("{:2d}".format(i * x), end=" ")
    print()