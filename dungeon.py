import sys
from random import randint

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer

from character import *
from monster import *
import event



player = NoClass()

form_class = uic.loadUiType("dungeon.ui")[0]
widgetchar_class = uic.loadUiType("character.ui")[0]
widgetcombat_class = uic.loadUiType("combat.ui")[0]

class CharWindowClass(QWidget, widgetchar_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.btn_warrior.clicked.connect(lambda: self.select_class("Warrior"))
        self.btn_mase.clicked.connect(lambda: self.select_class("Mase"))
        self.btn_assasin.clicked.connect(lambda: self.select_class("Assasin"))
        myWindow.txtLog.setPlainText("캐릭터를 선택해주세요.")

    def select_class(self, selclass):
        global player
        if selclass == "Warrior":
            player = Warrior()
        elif selclass == "Mase":
            player = Mase()
        else:
            player = Assasin()
        myWindow.txtLog.setPlainText(player.stats[0]+" 선택!")
        CharWindow.close()
        myWindow.show()
        
    def closeEvent(self, event):
        CombatWindow.btn_reset(1)
        CombatWindow.btn_reset(2)
        CombatWindow.btn_reset(3)
        myWindow.update_stats()

class WindowClass(QMainWindow, form_class):    #화면을 띄우는데 사용되는 Class 선언
    def __init__(self):
        super().__init__()
        self.stage = event.event_forest()
        self.setupUi(self)
        self.initUI()
                
    def initUI(self):
        self.txtLog.setAcceptRichText(True)
        self.btn_move.setEnabled(False)
        self.btn_item.setEnabled(False)
        self.btn_move.clicked.connect(self.moveEncounter)
        self.btn_item.clicked.connect(self.itemUse)
        self.progressBar_HP.setMinimum(0)
        self.btn_Charselect.clicked.connect(self.openCharwindow)
    
    def openCharwindow(self):
        self.btn_Charselect.setEnabled(False)
        self.btn_move.setEnabled(True)
        self.btn_item.setEnabled(True)
        myWindow.hide()
        CharWindow.show()

    def update_stats(self):
        self.progressBar_HP.setMaximum(player.stats[8])     # Player HP
        self.progressBar_HP.setValue(player.stats[7])
        self.lbl_Stat.setText(f'CLASS = {player.stats[0]}\n'
                              f'LEVEL = {player.stats[5]}\nHP = {player.stats[7]}\n'
                              f'STR = {player.stats[1]}\nINT = {player.stats[2]}\n'
                              f'DEX = {player.stats[3]}\nVIT = {player.stats[4]}\n'
                              f'EXP = {player.stats[6]}\nFHP = {player.stats[8]}')
        self.stage.event_stage1()
        self.txtLog.append("\n"+"<span style='color:green'>"+self.stage.event_msg+"</span>")

    def moveEncounter(self):
        self.txtLog.append("\n이동합니다.")
        self.encounterMonster()

    def printTextFunction(self):
        print(self.lbl_Stat.text())
    
    def itemUse(self):
        self.txtLog.append("물약을 사용하여, 체력을 회복합니다.\n")
        if player.stats[7] >= player.stats[8]:
                player.stats[7] = player.stats[8]
        else:
            player.stats[7] += 5
        self.update_stats()

    def encounterMonster(self):
        CombatWindow.show()
        self.hide()
        CombatWindow.combat_start()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '확인', '게임을 종료합니다.',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()

class CombatWindowClass(QWidget, widgetcombat_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.txtCombatLog.setAcceptRichText(True)
        self.btn_CombatAttack.clicked.connect(self.combat_attack)
        self.btn_CombatSkill1.clicked.connect(lambda: self.combat_skill(1))
        self.btn_CombatSkill2.clicked.connect(lambda: self.combat_skill(2))
        self.btn_CombatSkill3.clicked.connect(lambda: self.combat_skill(3))
        self.btn_reset(1)
        self.btn_reset(2)
        self.btn_reset(3)
        self.btn_CombatFlee.clicked.connect(self.combat_flee)
        self.bar_monsterhp.setMinimum(0)
        self.bar_playerhp.setMinimum(0)
        self.timerCombat = QTimer()
        self.timerSkill1 = QTimer()
        self.timerSkill2 = QTimer()
        self.timerSkill3 = QTimer()
        self.timerCombat.timeout.connect(self.monster_attack)
        self.timerSkill1.timeout.connect(lambda: self.skillTimer(1))
        self.timerSkill2.timeout.connect(lambda: self.skillTimer(2))
        self.timerSkill3.timeout.connect(lambda: self.skillTimer(3))
        self.timerSkill1.setInterval(1000)
        self.timerSkill2.setInterval(1000)
        self.timerSkill3.setInterval(1000)
        self.initTimer1 = 0
        self.initTimer2 = 0
        self.initTimer3 = 0
        self.monster_num = 0

    def combat_start(self):
        self.timerCombat.start()
        self.monster_num = self.monster_max_num = randint(1, 3)
        self.spawning_monster()

    def spawning_monster(self):
        self.monster = Monster()
        self.timerCombat.setInterval((6-self.monster.monster_speed) * 1000)
        self.lbl_MonsterSpeed.setText(str(self.monster.monster_speed))
        self.txtCombatLog.clear()
        self.update()
        msgSpawning = (f"\n{self.monster.monster_name}가 나타납니다. <span style='color: red'>({self.monster_num}/{self.monster_max_num})</span>")
        myWindow.txtLog.append(msgSpawning)
        CombatWindow.txtCombatLog.append(msgSpawning)


    def monster_attack(self):
        print("몬스터 어택!!")
        player.stats[7] -= self.monster.monster_damage()
        if player.stats[7] <= 0: player.stats[7] = 0 # - 수치를 0으로 바꿔줌
        combatmsg2 = f"{self.monster.monster_name}에게 <span style='color: red'><b> {str(self.monster.monster_damage)}</span></b> 의 피해를 입습니다!!\n"
        self.txtCombatLog.append(combatmsg2)
        myWindow.txtLog.append(combatmsg2)
        self.update()

    def combat_attack(self):
        for x in range(0, player.mulAttack):
            player_damage = randint(int(player.stats[1] / 2 / 5), int(player.stats[1]/5))

            self.monster.monster_hp -= player_damage
            if self.monster.monster_hp <= 0: self.monster_hp = 0 # - 수치를 0으로 바꿔줌
            if player.mulAttack >= 2:
                combatmsg1 = f"<span style='color: blue'><b>{str(player_damage)}</span>의 피해를 입힙니다!! (추가데미지)</b>"
            else:
                combatmsg1 = f"<span style='color: blue'><b>{str(player_damage)}</span></b>의 피해를 입힙니다!!"
            self.txtCombatLog.append(combatmsg1)
            self.update()

    def combat_skill(self, skillno):
        self.skillno = skillno
        skilldict = {1:player.skill_1, 2:player.skill_2, 3:player.skill_3}
        timerdict = {1:self.timerSkill1, 2:self.timerSkill2, 3:self.timerSkill3}
        timer = timerdict[self.skillno]
        skilldict[self.skillno]()
        self.skill_run(player.skillType)
        timer.start()

    def skill_run(self, type):
        if type == 0:                # 단타 타입
            self.monster.monster_hp -= player.skillPower
            self.txtCombatLog.append("<span style='color: green'><b>"+player.skillMsg+"</span>"+"<span style='color: blue'>"+str(-player.skillPower)+"</span></b>")
            self.update()
        elif type == 1:              # 더블어택류 타입
            self.txtCombatLog.append("<span style='color: green'><b>"+player.skillMsg+"</span></b>")
        elif type == 2:              # 도트 데미지
            self.txtCombatLog.append("<span style='color: green'><b>"+player.skillMsg+"</span></b>")
        elif type == 3:              # 방어력 상승
            self.txtCombatLog.append("<span style='color: green'><b>"+player.skillMsg+"</span></b>")
        elif type == 4:              # 힐링
            self.txtCombatLog.append("<span style='color: green'>"+player.skillMsg+"</span>")
            player.stats[7] += player.skillheal
            self.txtCombatLog.append(f"상처를 치료합니다. +{player.skillheal}")
            self.update()
        else:
            pass

    def skillTimer(self, skillno):
        self.skillno = skillno
        print(self.initTimer1)
        print(player.skillDuration, player.skillCooldown)
        if self.skillno == 1:
            if self.initTimer1 < player.skillDuration:
                self.btn_CombatSkill1.setText("활성화!!")
                self.btn_CombatSkill1.setEnabled(False)
                if player.skillType == 2:
                    self.monster.monster_hp -= player.skillDot
                    self.txtCombatLog.append(f"{player.skillName[skillno]} 데미지 - <span style='color:blue'>{player.skillDot}</span>")
                self.initTimer1 += 1
                self.update()
            elif self.initTimer1 == player.skillDuration:
                self.btn_CombatSkill1.setText("COOLDOWN")
                self.initTimer1 += 1
                player.skill_0()
            elif self.initTimer1 >= (player.skillDuration + player.skillCooldown):
                self.btn_CombatSkill1.setEnabled(True)
                self.timerSkill1.stop()
                self.btn_reset(skillno)
                self.initTimer1 = 0
            else:
                self.initTimer1 += 1

        if self.skillno == 2:
            if self.initTimer2 < player.skillDuration:
                self.btn_CombatSkill2.setText("활성화!!")
                self.btn_CombatSkill2.setEnabled(False)
                if player.skillType == 2:
                    self.monster.monster_hp -= player.skillDot
                    self.txtCombatLog.append(f"{player.skillName[skillno]} 데미지 - <span style='color:blue'>{player.skillDot}</span>")
                    self.update()
            elif self.initTimer2 == player.skillDuration:
                self.btn_CombatSkill2.setText("COOLDOWN")
                player.skill_0()
            elif self.initTimer2 >= (player.skillDuration + player.skillCooldown):
                self.btn_CombatSkill2.setEnabled(True)
                self.timerSkill2.stop()
                self.btn_reset(skillno)
            self.initTimer2 += 1

        if self.skillno == 3:
            if self.initTimer3 < player.skillDuration:
                self.btn_CombatSkill3.setText("활성화!!")
                self.btn_CombatSkill3.setEnabled(False)
                if player.skillType == 3:
                    self.monster.monster_hp -= player.skillDot
                    self.txtCombatLog.append(f"{player.skillName[skillno]} 데미지 - <span style='color:blue'>{player.skillDot}</span>")
                    self.update()
            elif self.initTimer3 == player.skillDuration:
                self.btn_CombatSkill3.setText("COOLDOWN")
                player.skill_0()
            elif self.initTimer3 >= (player.skillDuration + player.skillCooldown):
                self.btn_CombatSkill3.setEnabled(True)
                self.timerSkill3.stop()
                self.btn_reset(skillno)
            self.initTimer3 += 1

    def btn_reset(self, skillno):
        self.skillno = skillno
        btndict = {1:self.btn_CombatSkill1, 2:self.btn_CombatSkill2, 3:self.btn_CombatSkill3}
        btn = btndict[self.skillno]
        btn.setText(player.skillName[self.skillno])
        btn.setEnabled(True)
        if self.skillno == 1:
            self.initTimer1 = 0
        elif self.skillno == 2:
            self.initTimer2 = 0
        elif self.skillno == 3:
            self.initTimer3 = 0
        
    def update(self):
        self.lbl_monsterhp.setText(str(self.monster.monster_hp)+"/"+str(self.monster.monster_init_hp))
        self.lbl_playerhp.setText(str(player.stats[7])+"/"+str(player.stats[8]))
        self.bar_monsterhp.setMaximum(self.monster.monster_init_hp)        # Monster HP
        self.bar_monsterhp.setValue(self.monster.monster_hp)
        self.bar_playerhp.setMaximum(player.stats[8])     # Player HP
        self.bar_playerhp.setValue(player.stats[7])

        if self.monster.monster_hp <= 0:
            self.txtCombatLog.append(f"{self.monster.monster_name} 퇴치하였습니다.")
            myWindow.txtLog.append(f"{self.monster.monster_name} 퇴치하였습니다.")
            self.monster_num_sub()

    def combat_flee(self):
        self.combat_end()

    def monster_num_sub(self):
        self.monster_num -= 1
        if self.monster_num == 0:
            self.combat_victory()
        else:
            self.spawning_monster()

    def combat_victory(self):
        self.btn_reset(1)
        self.btn_reset(2)
        self.btn_reset(3)
        player.stats[6] += self.monster_max_num * 10
        myWindow.txtLog.append("\n"+str(self.monster_max_num * 10)+"의 경험치를 획득하였습니다.")
        if player.stats[6] >= player.stats[5]*20:
            player.levelup()
            myWindow.txtLog.append("\n<span style='color: red'><b>레벨이 올랐습니다!!</span></b>\n")
        self.combat_end()

    def combat_end(self):
        self.timerCombat.stop()
        self.timerSkill1.stop()
        self.timerSkill2.stop()
        self.timerSkill3.stop()
        self.initTimer1 = 0
        self.initTimer2 = 0
        self.initTimer3 = 0
        self.hide()
        myWindow.show()
        myWindow.update_stats()

if __name__ == "__main__" :
    app = QApplication(sys.argv)   # QApplication : 프로그램을 실행시켜주는 클래스

    myWindow = WindowClass()       # WindowClass의 인스턴스 생성
    CharWindow = CharWindowClass() # 캐릭터 선택창
    CombatWindow = CombatWindowClass() # 전투창
    
    myWindow.show()                # 프로그램 화면을 보여주는 코드
    app.exec_()                    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드