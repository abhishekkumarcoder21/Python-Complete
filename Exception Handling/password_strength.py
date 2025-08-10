def check_password_strength(password):
    if len(password)<8:
        raise Exception("Error: The password length must be more than 8 characters")
    
    print("Password is strong")

try:
    password=input("enter a password: ")
    check_password_strength(password)
except Exception as e:
    print(e)