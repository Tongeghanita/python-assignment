import math

# Functions for shapes
def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# Main program
print("Choose a shape to calculate area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    r = float(input("Enter radius of circle: "))
    print("Area of Circle:", area_circle(r))

elif choice == 2:
    l = float(input("Enter length of rectangle: "))
    w = float(input("Enter width of rectangle: "))
    print("Area of Rectangle:", area_rectangle(l, w))

elif choice == 3:
    b = float(input("Enter base of triangle: "))
    h = float(input("Enter height of triangle: "))
    print("Area of Triangle:", area_triangle(b, h))

else:
    print("Invalid choice! Please select 1, 2, or 3.")