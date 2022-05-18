CommonStats = [1, 0]
stats = []

class NoClass:
    def __init__(self):
        self.stats = ["NoClass", 0, 0, 0, 0, 0, 0 ,0, 0]
        self.skillName = ["", "", "", ""]
        self.mulAttack = 1
        self.skillPower = 1
        self.skilldef = 1
        self.skillheal = 1
        self.skillDuration = 1
        def levelup(self):
            pass

class Warrior(NoClass):
    def __init__(self):
        super().__init__()
        self.stats = ["Warrior", 10, 1, 3, 9]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
        self.skillName = ["", "배쉬", "트리플어택", "가드"]
    def levelup(self):
        self.stats[1] += 3
        self.stats[2] += 1
        self.stats[3] += 1
        self.stats[4] += 2
        self.stats[5] += 1
        self.stats[6] = 0
        self.stats[8] = self.stats[4] * 3
    def skill_00(self):
        self.skillDuration = 0
        self.skillCooldown = 0
        self.skillPower = self.stats[1]
    def skill_01(self):
        self.skillType = 0
        self.skillMsg = '무기를 높이 들어 강하게 내리칩니다!! "배쉬!!"'
        self.skillCooldown = 3
        self.mulpower = self.stats[1]
    def skill_02(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2
    def skill_03(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2

class Mase:
    def __init__(self):
        self.stats = ["Mase", 3, 10, 6, 3]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
        self.mulAttack = 1
        self.skillName = ["", "파이어볼", "라이트닝볼트", "힐링"]
    def levelup(self):
        self.stats[1] += 3
        self.stats[2] += 1
        self.stats[3] += 1
        self.stats[4] += 2
        self.stats[5] += 1
        self.stats[6] = 0
        self.stats[8] = self.stats[4] * 3
    def skill_00(self):
        self.skillDuration = 0
        self.skillCooldown = 0
        self.mulAttack = 1
    def skill_01(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2
    def skill_02(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2
    def skill_03(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2

class Assasin:
    def __init__(self):
        self.stats = ["Assasin", 6, 3, 10, 5]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
        self.mulAttack = 1
        self.skillName = ["", "더블어택", "백어택", "하이드"]
    def levelup(self):
        self.stats[1] += 3
        self.stats[2] += 1
        self.stats[3] += 1
        self.stats[4] += 2
        self.stats[5] += 1
        self.stats[6] = 0
        self.stats[8] = self.stats[4] * 3
    def skill_00(self):
        self.skillDuration = 0
        self.skillCooldown = 0
        self.mulAttack = 1
    def skill_01(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2
    def skill_02(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2
    def skill_03(self):
        self.skillDuration = 3
        self.skillCooldown = 3
        self.mulAttack = 2