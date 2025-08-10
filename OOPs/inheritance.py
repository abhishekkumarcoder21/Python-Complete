class Animal:
    def speak(self):
        print("Animals make sound")
class Dog(Animal):
    def bark(self):
        print("Dogs bark")

dog=Dog()
dog.speak()
dog.bark()