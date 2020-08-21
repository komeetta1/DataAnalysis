import math

def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    solution1 = (-b-math.sqrt(d))/(2*a)
    solution2 = (-b+math.sqrt(d))/(2*a)
    return (solution1, solution2)

print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1,2,1))