
# r = int(input("Radius of Area: "))

# # Destination Location
# x, y, z = input("Destination Location (x, y, z): ")

# # Camera Radius
# cameraRadius = int(input("Camera Radius: "))

from fallTime import FallTime
from distance import Distance

while True:
    h = int(input("H: "))

    if h != 0:
        v = int(input("V: "))

        t = FallTime(h).returner()
        print(t)

        x = Distance(v,t).returner()
        print(x)
    else:
        break