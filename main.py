class Stat:
    def __init__(self, value, minimum=0, maximum=10):
        self.value = value
        self.minimum = minimum
        self.maximum = maximum
        
    def __str__(self):
        return self.value

    def update(self):
        
        
class Pet:
    def __init__(self, name, species, hunger=5, happiness=0):
        self.name = name
        self.species = species
        self.hunger = Stat(hunger, 0, 10)
        self.happiness = Stat(hunger, 0, 10)

    def 
        
    def feed(self):
        if self.hunger == 0:
            print(f"{self.name} is already full!")
        else:
            self.hunger -= 3
            if self.hunger < 0:
                self.hunger = 0
            print(f"{self.name} was fed.")
        
    def play(self):
        if self.happiness == 10:
            print(f"{self.name} is already happy!")
        else:
            self.happiness += 5
            self.hunger += 3
            if self.happiness > 10:
                self.happiness = 10
            if self.hunger > 10:
                self.hunger = 10
            print(f"{self.name} was played with.")
        
    def __str__(self):
        stats_to_update = ((self.happiness, happiness_adjective), (self.hunger, hunger_adjective))
        for stat in stats_to_update:
        if stat[0] >= 10:
            stat[1] = "is extremely"
        elif stat[0] >= 5:
            stat[1] = "is quite"
        elif stat[0] > 0:
            stat[1] = "isn't very"
        else:
            stat[1] = "is not"

        return f"{self.name} the {self.species} {happiness_adjective} happy, and {hunger_adjective} hungry."

pets = [Pet("Daisy", "Dog"), Pet("Tom", "Cat"), Pet("Simon", "Human")]

pets[0].feed()
pets[1].play()
print(pets[2])

for x in range (0,5):
    pets[2].play()
    print(pets[2])

for x in range (0,5):
    pets[2].feed()
    print(pets[2])
