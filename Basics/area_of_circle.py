import math

PI=math.pi
radius=float(input("Enter the radius of circle: "))
if isinstance(radius,float):
    area=PI*radius**2
    print("The area of circle is ",area)

else:
    print("Wrong input...")
    