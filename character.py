CommonStats = [1, 0]

class NoClass:
    def __init__(self):
        self.stats = ["NoClass", 0, 0, 0, 0, 0, 0 ,0, 0]
        self.skillName = ["", "", "", ""]
        self.mulAttack = 1
        self.skillPower = 1
        self.skilldef = 1
        self.skillheal = 1
        self.skillDuration = 0
        def levelup(self):
            pass

class Warrior(NoClass):
    def __init__(self):
        super().__init__()
        self.stats = ["Warrior", 10, 1, 3, 9]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
        self.skillName = ["", "배쉬", "카운터", "가드"]
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
        self.skillPower = self.stats[1]
    def skill_02(self):
        self.skillType = 0
        self.skillMsg = '헛점을 노려 일격 "카운터!!"'
        self.skillDuration = 3
        self.skillCooldown = 3
        self.skillPower = self.stats[1]
    def skill_03(self):
        self.skillType = 3
        self.skillMsg = '전방에 방패 "가드!!"'
        self.skillDuration = 5
        self.skillCooldown = 5

class Mase(NoClass):
    def __init__(self):
        self.stats = ["Mase", 3, 10, 6, 3]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
        self.mulAttack = 1
        self.skillName = ["", "파이어볼", "라이트닝볼트", "힐링"]
    def levelup(self):
        self.stats[1] += 1
        self.stats[2] += 3
        self.stats[3] += 2
        self.stats[4] += 2
        self.stats[5] += 1
        self.stats[6] = 0
        self.stats[8] = self.stats[4] * 3
    def skill_00(self):
        self.skillDuration = 0
        self.skillCooldown = 0
        self.mulAttack = 1
    def skill_01(self):
        self.skillType = 2
        self.skillMsg = '도트 데미지 "파이어볼!!"'
        self.skillDuration = 4
        self.skillCooldown = 3
        self.skillDot = 2
    def skill_02(self):
        self.skillType = 0
        self.skillMsg = '전격 데미지 "라이트닝 볼트!!"'
        self.skillDuration = 0
        self.skillCooldown = 3
    def skill_03(self):
        self.skillType = 4
        self.skillMsg = '치료의 빛을 내린다 "힐링!!"'
        self.skillDuration = 0
        self.skillCooldown = 10
        self.skillheal = self.stats[2]/5

class Assasin(NoClass):
    def __init__(self):
        self.stats = ["Assasin", 6, 3, 10, 5]
        self.HP = self.FHP = self.stats[4] * 3
        self.stats += CommonStats
        self.stats += [self.HP, self.FHP]
        self.mulAttack = 1
        self.skillName = ["", "더블어택", "백어택", "하이드"]
    def levelup(self):
        self.stats[1] += 1
        self.stats[2] += 1
        self.stats[3] += 3
        self.stats[4] += 1
        self.stats[5] += 2
        self.stats[6] = 0
        self.stats[8] = self.stats[4] * 3
    def skill_00(self):
        self.mulAttack = 1
        self.skillPower = 1
        self.skilldef = 1
        self.skillheal = 1
    def skill_01(self):
        self.skillType = 1
        self.skillMsg = '쌍수 단검 "더블어택!!"'
        self.skillDuration = 2
        self.skillCooldown = 4
        self.mulAttack = 2
    def skill_02(self):
        self.skillType = 0
        self.skillMsg = '몰래 뒤로 돌아가 "백어택!!"'
        self.skillDuration = 0
        self.skillCooldown = 3
        self.skillPower = self.stats[3]
    def skill_03(self):
        self.skillType = 3
        self.skillMsg = '어둠 속에 몸을 가린다 "하이드!!"'
        self.skillDuration = 3
        self.skillCooldown = 5
        self.skilldef = 1