# Create your own game to practice object oriented programming concepts
import random
from statistics import mean

def randomize_sex():
    if random.randint(0,1) == 0:
        return True
    else:
        return False

class Horse:
    def __init__(self, name, breed, isMale, isAdult):
        self.name = name
        self.breed = breed
        self.male = isMale
        self.adult = isAdult
        self.level = 1
        self.competitions_won = 0
        self.needs_grooming = False
        self.times_groomed = 0
        self.assignAlias()

    def assignAlias(self):
        if self.adult:
            if self.male:
                self.gender_alias = "stallion"
            else:
                self.gender_alias = "mare"
        else:
            if self.male:
                self.gender_alias = "colt"
            else:
                self.gender_alias = "filly"

    def __repr__(self):
        return "This is the {gender} {name}. They are a {breed} at level {level} and have won {competitions_won} competitions.".format(gender=self.gender_alias, name=self.name, breed=self.breed, level=self.level, competitions_won=self.competitions_won)

    def groomHorse(self):
        self.needs_grooming = False
        self.times_groomed += 1
        if self.times_groomed == 3 and not self.adult:
            self.adult = True
            print("Your horse grew up from a foal to an adult!")
        self.assignAlias()

    def competeHorse(self):
        compet_int = random.randint(0, 1)
        if compet_int == 0:
            self.competitions_won += 1
            print("You won the competition! {name} has won {comp_won} competitions total.".format(name=self.name, comp_won=self.competitions_won))
            if self.competitions_won % 2 == 0:
                self.level += 1
                print("{name} leveled up!".format(name=self.name))
        else:
           print("Sorry, you lost the competition. Better luck next time.")

class Trainer:
    def __init__(self, name):
        self.name = name
        self.horses = []

    def __repr__(self):
        return "This is the trainer {name}. They own {num_horses} horses.".format(name=self.name, num_horses=len(self.horses))

    def addHorse(self, horse):
        self.horses.append(horse)

    def listHorses(self):
        horse_list = ""
        for horse in self.horses:
            horse_list += (horse.name + "    ")
        print(horse_list)

    def viewStable(self):
        for horse in self.horses:
            print(horse)

    def groomHorse(self):
        print("Which horse do you want to groom?")
        self.listHorses()
        horse_to_groom = input("")
        for horse in self.horses:
            if horse.name == horse_to_groom:
                horse.groomHorse()
                print("You groomed {name}.".format(name=horse.name))
                #print(horse)

    def competeHorse(self):
        print("Which horse do you want to compete?")
        self.listHorses()
        horse_to_compete = input("")
        for horse in self.horses:
            if horse.name == horse_to_compete:
                horse.competeHorse()

    def breedHorse(self):
        print("Which stallion do you want to breed?")
        stallion_list = ""
        for horse in self.horses:
            if horse.male and horse.adult:
                stallion_list += (horse.name + "    ")
        print(stallion_list)
        stallion_to_breed = input("")
        for horse in self.horses:
            if horse.name == stallion_to_breed:
                stallion_to_breed = horse

        print("Which mare do you want to breed?")
        mare_list = ""
        for horse in self.horses:
            if horse.adult and not horse.male:
                mare_list += (horse.name + "    ")
        print(mare_list)
        mare_to_breed = input("")
        for horse in self.horses:
            if horse.name == mare_to_breed:
                mare_to_breed = horse
        
        def randomize_breed():
            if random.randint(0,1) == 0:
                return "quarter horse"
            else:
                return "mustang"

        # foal_level = mean([stallion_to_breed.level, mare_to_breed.level])
        name_of_foal = input("What do you want to name your foal?\n")
        new_foal = Horse(name_of_foal, randomize_breed(), randomize_sex(), False)
        self.addHorse(new_foal)
        print(new_foal)

# Testing classes

# trainer_name = "Isabel"
# print("Hi " + trainer_name + ", are you ready to play?")
# trainer1 = Trainer(trainer_name)
# horse1_name = "Daisy"
# horse2_name = "Spirit"
# horse3_name = "Cloud"

# Playing the game
trainer_name = input("Welcome to your stable. Enter your name below. \n")
print("Hi " + trainer_name + ", are you ready to play?")
trainer1 = Trainer(trainer_name)
horse1_name = input("What do you want to name your first horse? She is a quarter horse mare.\n")
horse2_name = input("What do you want to name your second horse? He is a mustang stallion. \n")
horse3_name = input("What do you want to name your first foal? They are a quarter horse filly.\n")
mare1 = Horse(horse1_name, "quarter horse", False, True)
stallion1 = Horse(horse2_name, "mustang", True, True)
foal1 = Horse(horse3_name, "quarter horse", False, False)
trainer1.addHorse(mare1)
trainer1.addHorse(stallion1)
trainer1.addHorse(foal1)

while True:
    action = input("What do you want to do? You can view stable, groom, breed, or compete. Type your answer below.\n")
    if action == 'groom':
        trainer1.groomHorse()
    if action =='compete':
        trainer1.competeHorse()
    if action == 'view stable':
        trainer1.viewStable()
    if action == 'breed':
        trainer1.breedHorse()
    if action == "exit":
        print("Thanks for playing!")
        break
# To Do