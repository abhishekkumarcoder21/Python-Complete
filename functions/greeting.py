# positional argument
# keyword argument
# default argument


def welcome(name="bittubhai",city="Gurgaon"):
    print(f"Welcome {name} in {city}")

def say_greet(name): #parameter
    print(f"hello {name}! good morning.")

say_greet("Abhishek") #argument

say_greet("bittu raja")

welcome("Abhishek","Bengalore")
welcome(city="Hyderabad",name="Bitturaja")
welcome()