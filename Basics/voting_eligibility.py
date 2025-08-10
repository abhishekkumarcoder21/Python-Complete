age=int(input("Enter your age: "))
if age>=18 and age<=100:
    print("You can drive.")
elif age<18 and age>0:
    print("You are a kid..so cannot drive")
else:
    print("Invalid age.")