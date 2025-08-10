class Car:
    def __init__(self,name):
        self.name=name
    def start(self):
        print(f"{self.name} is starting......")

    def stop(self):
        print(f"{self.name} is stopping......")

brio=Car("Brio")
swift=Car("Swift")

brio.start()
brio.stop()

swift.start()
swift.stop()