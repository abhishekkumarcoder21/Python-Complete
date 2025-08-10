with open('text3.txt','a') as file:
    content=input("Enter data: ")
    file.write(content)
    print("Saved!")