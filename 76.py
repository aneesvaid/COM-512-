# write a python program to store two points as tuples and calculate the distance between them.
import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

point1 = (x1, y1)
point2 = (x2, y2)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Point 1:", point1)
print("Point 2:", point2)
print("Distance:", distance)