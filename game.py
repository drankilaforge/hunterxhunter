class HunterRPG: def init(self, character, life, weapon): self.character = character self.life = life self.weapon = weapon

def hunting(self, animal_health):
    if self.weapon == "Axe":
        character_damage = 50
        kill = animal_health - character_damage
        print(f"Animal health is now {kill} and it was slain by player {self.character} who had the weapon {self.weapon}".format())

    elif self.weapon == "Katana":
        character_damage = 75
        kill = animal_health - character_damage
        print(f"Animal health is now {kill} and it was slain by player {self.character} who had the weapon {self.weapon}".format())

    elif self.weapon == "Crossbow":
        character_damage = 100
        kill = animal_health - character_damage
        print(f"Animal health is now {kill} and it was slain by player {self.character} who had the weapon {self.weapon}".format())

    else:
        print(f"Failed to pick a weapon which exists, animal has killed {self.character}")

def healing(self, potion_power):
    boosted_health = self.life + potion_power
    print(f"Your health bars are now {boosted_health}")

loop = True 
while loop: 
    select_weapon = input("Choose A Weapon: ")
    player1 = HunterRPG("Chucky", 100, select_weapon) 
    player1.hunting(101) 
    player1.healing(85)