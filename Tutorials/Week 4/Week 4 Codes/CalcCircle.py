import math
pi = math.pi

print("(1) Calculate area of circle >>")
print("(2) Calculate volume of sphere >>")

ch1 = int(input("Enter your option >>"))

def calcArea(radius):
    area = pi * (radius ** 2)
    return round(area, 2)

def calcVolume(radius):
    volume = (4/3) * pi * (radius ** 3)
    return round(volume, 2)

if ch1 == 1:
    radius = float(input("Enter the radius of the circle >>"))
    print("The area of the circle is", calcArea(radius))
elif ch1 == 2:
    radius = float(input("Enter the radius of the sphere >>"))
    print("The volume of the sphere is", calcVolume(radius))