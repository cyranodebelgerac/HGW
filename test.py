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
        self.hp = int(self.hp - saba_atk * modifier)
    def heal(self, amount):
        self.hp =int(self.hp + amount)

###########################################################
# list of servants
saba = [
        Servant("Artoria Pendragon", "Saber", 10000, 1000, "5"), 
        Servant("EMIYA", "Archer", 8500, 900, "4"),
        Servant("Cu Chulainn", "Lancer", 9000, 1050, "3"),
        Servant("Medusa", "Rider", 10000, 1000, "3"),
        Servant("Sasaki Kojirou", "Assassin", 9000, 1200, "1"),
        Servant("Medea", "Caster", 8500, 900, "3"),
        Servant("Heracles", "Berserker", 10000, 1000, "4"),
        Servant("Jeanne D'arc", "Ruler", 12000, 600, "5"),
        Servant("Angra Mainyu", "Avenger", 6000, 600, "3"),
        Servant("BB", "Moon Cancer", 10000, 1000, "4")
        ]

# generates a string with all servants' names separated by a comma. Used in servant_select
saba_list = ""
for x in range(len(saba)):
    saba_list = saba_list + saba[x].name + ", "

###########################################################
# player inputs a servant name, determines that it's valid. Used at the beginning of the war.
def servant_select():
    choice = "   "
    while choice + "," not in saba_list.upper():
        choice = input("Choose a servant: \n").upper()
    return choice

# takes in servant name (verified by servant_selection) and returns an actual servant
def set_servant(name):
    for x in range(len(saba)):
        if name == saba[x].name.upper():
            return saba[x]
        
# returns a random servant
def rand_servant():
    return saba[random.randint(0,len(saba) - 1)]

# determines class advantage dmg. these next two functions go together.
# in case of nero caster's skill, do modifier = modifier/modifier i guess? 
def reg_adv_modifier(enemy_class, adv, disadv, berserker):
    if enemy_class in adv:
        return 2
    if enemy_class in disadv:
        return 0.5
    if berserker:
        return 1.5
    
def class_adv(saba_class, enemy_class):
    if saba_class == "Saber":
        return reg_adv_modifier(enemy_class, "Archer", "Lancer", 1)
    if saba_class == "Archer":
        return reg_adv_modifier(enemy_class, "Lancer", "Saber", 1)
    if saba_class == "Lancer":
        return reg_adv_modifier(enemy_class, "Saber", "Archer", 1)
    if saba_class == "Rider":
        return reg_adv_modifier(enemy_class, "Assassin", "Caster", 1)
    if saba_class == "Assassin":
        return reg_adv_modifier(enemy_class, "Caster", "Rider", 1)
    if saba_class == "Caster":
        return reg_adv_modifier(enemy_class, "Rider", "Assassin", 1)
    if saba_class == "Berserker":
        return 2
    if saba_class == "Ruler":
        return reg_adv_modifier(enemy_class, "Avenger", "Moon CancerSaberArcherLancerRiderAssassinCaster", 1)
    if saba_class == "Avenger":
        return reg_adv_modifier(enemy_class, "Moon Cancer", "Ruler", 1)
    if saba_class == "Moon Cancer":
        return reg_adv_modifier(enemy_class, "Ruler", "Avenger", 1)
    return 1

def combat(player, enemy):
    modifier = class_adv(player.servant_class, enemy.servant_class)
    player.take_dmg(enemy.atk, modifier)
    print("{} attacks! {} takes {} damage!".format(enemy.name,player.name, int(enemy.atk * modifier)))

def victory(servant):
    if servant.hp <= 0:
        return 1
            
###########################################################
print("Welcome to the Holy Grail War!")

choice = "  "
player = set_servant(servant_select())
enemy = rand_servant()

turn = 1

while 1:
    print("*"*10 + "Turn {}".format(turn) + "*"*10)
    print("{} has {} HP left!".format(player.name, player.hp))
    print("{} has {} HP left!".format(enemy.name, enemy.hp))
    print("*"*10)
    
    combat(player, enemy)
    if victory(player):
        winner = enemy
        break
    
    combat(enemy, player)
    if victory(enemy):
        winner = player
        break
    else:
        turn += 1
        input("")
        
print("---------------------")
print("{} has won!".format(winner.name))
