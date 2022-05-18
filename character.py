CommonStats = [1, 0]
stats = []

class Player:
    def __init__(self):
        self.stats = ["Warrior", 10, 1, 3, 9]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
        self.mulAttack = 1
        self.skillName = ""
    def levelup(self):
        self.stats[1] += 3
        self.stats[2] += 1
        self.stats[3] += 1
        self.stats[4] += 2
        self.stats[5] += 1
        self.stats[6] = 0
        self.stats[8] = self.stats[4] * 3
    def skill_00(self):
        self.skillName = ""
        self.skillDuration = 0
        self.skillCooldown = 0
        self.mulAttack = 1
    def skill_01(self):
        self.skillName = "더블어택"
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2
    def skill_02(self):
        self.skillName = "트리플어택"
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2

        combatSkill_02 = "승룡권"
        combatSkill_03 = "용권선풍각"

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