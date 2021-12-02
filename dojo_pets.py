class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food, pet) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print (f"{self.first_name} {self.last_name} walked {self.pet.name} ")
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name} {self.last_name} fed {self.pet.name} ")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.first_name} {self.last_name} gave {self.pet.name} a bath")
        self.pet.noise()
        return self

    #- walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

class Pet:
    def __init__(self, name , type , tricks, health, energy, sound) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    def sleep(self):
        self.energy += 25 
        print(f"{self.name} took a nap health is now: {self.health}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} chowed down\nenergy + 5 {self.energy}\nhealth +10 {self.health}")
        return self

    def play(self):
        self.health += 5
        print(f"{self.name} threw the frisbee!!!!\nHealth +5: {self.health}")
        return self

    def noise(self):
        print(self.sound)

patches = Pet("patches", "dog", "dance", 100, 70, "yip, yip")
fuma_kotaro = Ninja("Fuma", "Kotaro", "bones", "dog chow", patches)

fuma_kotaro.walk()
fuma_kotaro.feed()
fuma_kotaro.bathe()

# patches.sleep()
# patches.eat()
# patches.play()
# patches.noise()