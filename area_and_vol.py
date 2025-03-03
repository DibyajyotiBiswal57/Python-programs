import math

# Area of a rectangle
len=float(input("Enter the length of the rectangle: "))
bre=float(input("Enter the breadth of the rectangle:"))

area=len*bre

print(f"The area of the rectangle is {area}.")

# Area of a cirle
rad=float(input("Enter the radius of the circle: "))

area = math.pi*rad**2

area = round(area, 2)

print(f"The area of the circle is approximately {area}.")