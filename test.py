import math

x1 = 0
y1 = 0

x2 = 1
y2 = math.sqrt(1 - x2*x2)

i = 0
while i < 2:
    x2 = 1 - i
    y2 = math.sqrt(1 - x2*x2)   
    track_angle = math.degrees(math.atan2(-0.1, -1))
    i += 0.1
    print(track_angle)

a = True
if a == True:
    print("YES")

