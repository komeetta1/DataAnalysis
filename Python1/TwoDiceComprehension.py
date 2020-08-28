
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

L = [print(i,y) for i in dice1
    for y in dice2
    if i + y == 5]
