import random

###########################################################
# set basic parameters for a servant. 
class Servant:
    def __init__(self, name, servant_class, hp, atk, rarity):
        self.name = name
        self.servant_class = servant_class
        self.hp = hp
        self.atk = atk
        self.rarity = rarity
    def take_dmg(self, saba_atk, modifier):
        self.hp = self.hp - saba_atk * modifier

###########################################################
# list of servants
saba = [
        Servant("Artoria Pendragon", "Saber", 10000, 1000, "5"), 
        Servant("EMIYA", "Archer", 8500, 900, "4"),
        Servant("Cu Chulainn", "Lancer", 9000, 950, "3"),
        Servant("Medusa", "Rider", 10000, 1000, "3"),
        Servant("Sasaki Kojirou", "Assassin", 9000, 1200, "1"),
        Servant("Medea", "Caster", 8500, 900, "3"),
        Servant("Heracles", "Berserker", 10000, 1000, "4")
        ]

# generates a string with all servants' names separated by a comma. 
saba_namelist = ""
for x in range(len(saba)):
	saba_namelist = saba_namelist + saba[x].name+ ", "

###########################################################
# player inputs a servant name, determines that it's valid
def servant_selection():
    choice = "   "
    while choice + "," not in saba_namelist.upper():
        choice = input("Choose a servant: \n").upper()
    return choice

# takes in servant name (verified by servant_selection) and returns an actual servant
def set_servant(name):
    for x in range(len(saba)):
        if name == saba[x].name.upper():
            return saba[x]
        
# returns a random servant
def rand_servant():
    return saba[random.randint(1,len(saba) - 1)]

def class_adv(saba_class, enemy_class):
    if saba_class == "Saber":
        if enemy_class == "Archer":
            return 2
        if enemy_class == "Berserker":
            return 1.5
    if saba_class == "Archer":
        if enemy_class == "Lancer":
            return 2
        if enemy_class == "Berserker":
            return 1.5
        return 1
    if saba_class == "Lancer":
        if enemy_class == "Saber":
            return 2
        if enemy_class == "Berserker":
            return 1.5
    if saba_class == "Rider":
        if enemy_class == "Assassin":
            return 2
        if enemy_class == "Berserker":
            return 1.5
    if saba_class == "Assassin":
        if enemy_class == "Caster":
            return 2
        if enemy_class == "Berserker":
            return 1.5
        return 1
    if saba_class == "Caster":
        if enemy_class == "Rider":
            return 2
        if enemy_class == "Berserker":
            return 1.5
    if saba_class == "Berserker":
        return 2
    return 1
            
###########################################################
print("Welcome to the Holy Grail War!")

choice = "  "
player_choice = servant_selection()
player = set_servant(player_choice)
enemy = rand_servant()

modifier = class_adv(player.servant_class, enemy.servant_class)
enemy_modifier = class_adv(enemy.servant_class, player.servant_class)

while player.hp > 0 or enemy.hp > 0:
    print("*"*10)
    print("{} has {} HP left!".format(player.name, player.hp))
    print("*"*10)
    print("{} has {} HP left!".format(enemy.name, enemy.hp))
    print("*"*10)
    
    player.take_dmg(enemy.atk, modifier)
    print("{} attacks! {} takes {} damage!".format(enemy.name,player.name, enemy.atk * modifier))
    if player.hp <= 0:
        input("---------------------")
        print("{} has won!".format(enemy.name))
        break
        
    enemy.take_dmg(player.atk, enemy_modifier)
    print("{} attacks! {} takes {} damage!".format(player.name,enemy.name, player.atk * enemy_modifier))
    if enemy.hp <= 0:
        input("---------------------")
        print("{} has won!".format(player.name))
        break
    input("---------------------")
