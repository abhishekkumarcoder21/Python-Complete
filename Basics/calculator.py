a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

choice=(input("Enter + for addition\nEnter - for subtraction\nEnter * for multiplication\nEnter / for division\n"))
if choice=='+':
    print(f"{a+b}")
elif choice=='-':
    print(f"{a-b}")
elif choice=='*':
    print(f"{a*b}")
elif choice=='/':
    print(f"{a/b}")
else:
    print("invalid choice")
