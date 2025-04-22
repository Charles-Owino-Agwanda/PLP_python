class Vehicle:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
    
    def show(self):
        print(F"I am {self.name} and I'm powered by {self.fuel}")
    
    def move(self):
        print("I don't know my type of movement")

class Car(Vehicle):
    def move(self):
        print("I move by Driving on the road")
        
class Plane(Vehicle):
    def move(self):
        print("I move by flying through the air")

class Ship(Vehicle):
    def move(self):
        print("I move by Yawing/Rolling on water")

class Tanker(Vehicle):
    pass

print("-" * 15 + "Use case car" + "-" * 15)
c = Car("Toyota", "Petrol")
c.show()
c.move()

print("\n")
print("-" * 15 + "Use case Plane" + "-" * 15)
p = Plane("Boeing", "Jet Fuel/Kerosine")
p.show()
p. move()

print("\n")
print("-" * 15 + "Use case Ship" + "-" * 15)
s = Ship("MV Harambee", "Diesel")
s.show()
s.move()

print("\n")
print("-" * 15 + "Use case Tanker" + "-" * 15)
T = Tanker("Tanker", "Diesel")
T.show()
T.move()

print("-" * 50)