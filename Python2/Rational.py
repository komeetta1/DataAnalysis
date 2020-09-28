
class rational():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.num1}/{self.num2}"

    def __add__(self, numb):
        new_num2 = int(self.num2) * int(numb.num2)
        mult1 = new_num2 / self.num2
        mult2 = new_num2 / numb.num2
        new_num1 = int(mult1 * int(self.num1) + mult2 * int(numb.num1))
        return rational(new_num1, new_num2)

    def __sub__(self, numb):
        new_num2 = int(self.num2) * int(numb.num2)
        mult1 = new_num2 / self.num2
        mult2 = new_num2 / numb.num2
        new_num1 = int(mult1 * int(self.num1) - mult2 * int(numb.num1))
        return rational(new_num1, new_num2)

    def __mul__(self, numb):
        new_num2 = int(self.num2 * numb.num2)
        new_num1 = int(self.num1 * numb.num1)
        return rational(new_num1, new_num2)

    def __truediv__(self, numb):
        new_num1 = int(self.num1 * numb.num2)
        new_num2 = int(self.num2 * numb.num1)
        return rational(new_num1, new_num2)

    def __eq__(self, numb):
        return self.num1 == numb.num1 and self.num2 == numb.num2

    def __gt__(self,numb):
        new_num2 = int(self.num2) * int(numb.num2)
        mult1 = new_num2 / self.num2
        mult2 = new_num2 / numb.num2
        return mult1 * self.num1 > mult2 * self.num2

    def __lt__(self, numb):
        new_num2 = int(self.num2) * int(numb.num2)
        mult1 = new_num2 / self.num2
        mult2 = new_num2 / numb.num2
        return mult1 * self.num1 < mult2 * self.num2

def main():
    r=rational(1,4)
    r2 = rational(2,3)
    print(r)
    print(r2)
    print(r + r2)
    print(r - r2)
    print(r * r2)
    print(r / r2)
    print(rational(1,2) == rational(2,4))
    print(rational(1,2) > rational(2,4))
    print(rational(1,2) < rational(2,4))


if __name__ == "__main__": 
    main() 