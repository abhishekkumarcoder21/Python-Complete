lst=[1,2,3,5,4,6,8,7,9,10,15,14,12,20]
choice=int(input("enter a number to check whether it is present in the list or not: "))
if choice in lst:
    print(f"Yes, {choice} is present in the list")
else:
    print(f"No, {choice} is not present in the list")
    