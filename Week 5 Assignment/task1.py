#Task 1: Create A class

class Pet:                  #Class created is named pet
    def __init__(self, name, age):    #Constructor is used to initialize each object with unique values
        self.name = name
        self.age = age

# Methods added to the class include show and speak  
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    
    def speak(self):
        print("I don't know what to say")
        
class Dog(Pet):     # A new class called Cat created to demonstrate inheritance
    def speak(self):
        print("Bark")

class Cat(Pet):    # A new class called Cat created to demonstrate inheritance
    def __init__(self, name, age, color):
        Pet.__init__(self, name, age)
        self.color = color
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        
    def speak(self):
        print("meow")
        
class fish(Pet):
    pass
# Use case 1: Super class       
p = Pet("Tim", 19)
p.show()

#Use case 2: Cat sub class
c = Cat("Bill", 34, "Brown")
c.show()
c.speak()

#Use case 3: Dog subclass
d = Dog("Bosco", 34)
d.show()
d.speak()

#Use case 4: Fish Subclass
e = fish("Fis", 20)
e.show()
e.speak()
