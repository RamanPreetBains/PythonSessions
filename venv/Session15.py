class Parent:
    def showVehicle(self):
        print("Vehicle is Maruti Swift")

class Child(Parent):   #Child(Parent) -> Linking (IS-A)
    def showVehicle(self):
        pass
        """print("Vehicle is Honda City")"""


print(Parent.__dict__)
print(Child.__dict__)

ch = Child()
ch.showVehicle()

print(ch.__dict__)
