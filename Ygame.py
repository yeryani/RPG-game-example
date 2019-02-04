class Person:
    def __init__ (self, name, hp, mp, atk, magic):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.maxmp =mp
        self.mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Physical Attack", "Magic"]
        self.magic = magic

    def stats(self):
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        print(f"{self.mp}/{self.maxmp}")

    def generate_atk_damage(self):
        dmg = random.randint(self.atk_low, self.atk_high)
#read the rand range and radn int and the difference between them in the random description in the material
        return dmg

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
# self hitpoint is self hp minus the damage
        if self.hp < 0:
            self.hp = 0
    # can't go in the negative, so if less than 0 keep it 0
        return self.hp

    def choose_action(self):
    #one option is to list different actions    print("1. Attack") print("2")..etc
    #but it's better to create an index
        index= 1
        print ("ACTIONS: ")
        for element in self.action:
            print("{}. {}".format(index, element))
            index = index + 1

    def reduce_mp(self, used_mp):
        self.mp = self.mp - used_mp
        return self.mp

    def choose_magic(self):
        index = 1
        print ("Magic ")
        print ("ACTIONS: ")
        for element in self.magic:
            print("{}. {}".format(index, element))
            index = index + 1
