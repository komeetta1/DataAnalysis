import math

while True:
    shape=input("Choose a shape (triangle, rectangle, circle):")

    if shape == "triangle":
        base = int(input("Give base of the triangle: "))
        height = int(input("Give height of the triangle: "))
        print("The area is ", base*height/2)
    elif shape == "rectangle":
        width = int(input("Give width of the rectangle: "))
        height = int(input("Give height of the rectangle: "))
        print("The are is ", width*height)
    elif shape == "circle":
        radius = int(input("Give radius of the circle: "))
        print("The area is ", math.pi*radius**2)
    elif shape == " ":
        break
    else:
        print("Unknown shape!")

