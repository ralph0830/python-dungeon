from random import *
import os

def lvl_up(self):
    if self.exp >= 10 * self.lvl:
        self.lvl += 1
        print('축하합니다! 레벨', self.lvl, '이 되었습니다!\n능력치가 상승하였습니다.')
        self.str += 2
        self.dex += 1
        self.vit += 2
        self.fhp += 5
        self.exp = 0
        self.stat()


def use_item(self):
    self.hp += 5
    if self.hp > self.fhp:
        self.hp = self.fhp
        print("물약을 사용합니다. 체력이 가득찼습니다.", self.hp, "/", self.fhp, "\n")
    else:
        print("물약을 사용합니다. 체력이 5 회복됩니다.", self.hp, "/", self.fhp, "\n")