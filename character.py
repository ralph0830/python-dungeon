CommonStats = [1, 0]
stats = []

class Player:
    def __init__(self):
        self.stats = ["Warrior", 10, 1, 3, 9]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
    def levelup(self):
        self.stats[1] += 3
        self.stats[2] += 1
        self.stats[3] += 1
        self.stats[4] += 2
        self.stats[5] += 1
        self.stats[6] = 0
        self.stats[8] = self.stats[4] * 3
    def skill(self, skillnum):
        WarriorSkill_1 = "파동권"
        WarriorSkill_2 = "승룡권"
        WarriorSkill_3 = "용권선풍각"

class NoClass:
    stats = ["NoClass", 0, 0, 0, 0, 0, 0 ,0, 0]
    def levelup(self):
        pass

class Warrior:
    CLASS = "Warrior"

class Mase:
    stats = ["Mase", 3, 10, 6, 3, 20, 1, 0, 20]

class Assasin:
    stats = ["Assasin", 6, 3, 10, 5, 25, 1, 0, 25]