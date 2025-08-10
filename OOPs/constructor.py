class Car:
    def __init__(self,name,colour,engine):
        self.name=name
        self.colour=colour
        self.engine=engine

car1=Car("Scorpio","White",2500)
print(car1.name,car1.colour,car1.engine)


# default constructor (self)
# parameterized constructor (name,colour)
# constructor with default values (name="yourname", colour="red")