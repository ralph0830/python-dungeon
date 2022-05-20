from random import choice, randint

class Monster():
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        monsters = "코볼트", "고블린", "좀비", "구울"
        self.monster_name = choice(monsters)
        self.monster_speed = randint(1, 5)
        self.monster_hp = randint(1, 30)
        self.monster_init_hp = self.monster_hp
        
    def monster_damage(self):
        return randint(1, 3)

