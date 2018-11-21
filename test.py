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

def servant_selection():
    choice = ""
    while choice not in (saba001.name,saba002.name,saba003.name,saba004.name,saba005.name,saba006.name,saba007.name):
        choice = input("Choose a servant: \n")
    for x in (saba001,saba002,saba003,saba004,saba005,saba006,saba007):
        if choice == x.name:
            return x

def enemy_selection():
    choice = ""
    while choice not in (saba001.name,saba002.name,saba003.name,saba004.name,saba005.name,saba006.name,saba007.name):
        choice = input("Choose an enemy: \n")
    for x in (saba001,saba002,saba003,saba004,saba005,saba006,saba007):
        if choice == x.name:
            return x

            
###########################################################


saba001 = Servant("Artoria Pendragon", "Saber", 10000, 1000, "5")
saba002 = Servant("EMIYA", "Archer", 8500, 900, "4")
saba003 = Servant("Cu Chulainn", "Lancer", 8500, 900, "4")
saba004 = Servant("Medusa", "Rider", 10000, 1000, "5")
saba005 = Servant("Sasaki Kojirou", "Assassin", 9000, 1200, "4")
saba006 = Servant("Medea", "Caster", 8500, 900, "4")
saba007 = Servant("Heracles", "Berserker", 10000, 1000, "5")


###########################################################

print("Welcome to the Holy Grail War!")

player = servant_selection()

enemy = enemy_selection()

modifier = class_adv(player.servant_class, enemy.servant_class)
enemy_modifier = class_adv(enemy.servant_class, player.servant_class)

while player.hp > 0 or enemy.hp > 0:
    print("{} has {} HP left!".format(player.name, player.hp))
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
