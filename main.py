
import math

coordinates1 = int(input("x1:"))
coordinates2 = int(input("x2:"))
coordinates3 = int(input("y1:"))
coordinates4 = int(input("y2:"))

distances = math.hypot(abs(coordinates1-coordinates2), abs(coordinates3-coordinates4))

print(distances)
