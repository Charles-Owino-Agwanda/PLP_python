class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
            
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10

    def sleep(self):
        self.energy += 5
        if self.energy > 10:
            self.energy = 10

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
        
        self.happiness += 2
        self.hunger += 1
        
        if self.happiness > 10:
            self.happiness = 10
        if self.hunger > 10:
            self.hunger = 10

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness += 1
        if self.happiness  > 10:
            self.happiness  = 10

    def show_tricks(self, trick):
        if trick in self.tricks:
            print(f" Yes! {self.name} knows how to {trick}. 🐾")
        else:
            print(f"{self.name} doesn't know how to {trick} yet.")
        

    def get_status(self):
        print(f"🐶 {self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print("-" * 25)
     
        
if __name__ == "__main__":
    pet = Pet("Buddy")
    pet.get_status()
    pet.train("roll over")
    pet.train("sit")
    pet.show_tricks("roll over")
    pet.show_tricks("fetch")