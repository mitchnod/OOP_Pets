class Pet:
    health = 100
    energy = 100
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def speak(self):
        print(self.noise)
    def check_up(self):
        print(f"Energy: {self.energy} Health: {self.health}")

class Owner:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.speak()


charli = Pet("Charli", "Cat", "Play dead", "meow")
mitch = Owner("Mitch", "Nodland", charli, "Treat", "Cat Food")

mitch.walk()
charli.check_up()