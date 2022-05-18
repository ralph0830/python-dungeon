import sys
from random import *
from xml.sax.handler import DTDHandler
from PyQt5.QtWidgets import *
from PyQt5 import uic
from character import *

player = NoClass()
monster_name = ""

form_class = uic.loadUiType("dungeon.ui")[0]
widgetchar_class = uic.loadUiType("character.ui")[0]
widgetcombat_class = uic.loadUiType("combat.ui")[0]

class CharWindowClass(QWidget, widgetchar_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_warrior.clicked.connect(lambda: self.select_class("Warrior"))
        # self.btn_mase.clicked.connect(lambda: self.select_class("Mase"))
        # self.btn_assasin.clicked.connect(lambda: self.select_class("Assasin"))

    def select_class(self, selclass):
        global player
        if selclass == "Warrior":
            player = Player()
        elif selclass == "Mase":
            player = Mase()
        else:
            player = Assasin()
        strclass = str(f'CLASS = {player.stats[0]}\n'
                              f'LEVEL = {player.stats[5]}\nHP = {player.stats[7]}\n'
                              f'STR = {player.stats[1]}\nINT = {player.stats[2]}\n'
                              f'DEX = {player.stats[3]}\nVIT = {player.stats[4]}\n'
                              f'EXP = {player.stats[6]}\nFHP = {player.stats[8]}\n')
        myWindow.txtLog.setPlainText(strclass)
        CharWindow.close()
        myWindow.show()
        
    def closeEvent(self, event):
        myWindow.update_stats()

class WindowClass(QMainWindow, form_class):    #화면을 띄우는데 사용되는 Class 선언
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.update_stats()
        self.btn_move.clicked.connect(self.moveEncounter)
        self.btn_item.clicked.connect(self.itemUse)
        self.progressBar_HP.setMinimum(0)
        self.btn_Charselect.clicked.connect(self.openCharwindow)
    
    def openCharwindow(self):
        self.btn_Charselect.setEnabled(False)
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

    def moveEncounter(self):
        if isinstance(player, NoClass) == True:
            self.btn_Charselect.setEnabled(False)
            myWindow.hide()
            CharWindow.show()
        else:
            CombatWindow.update()
            self.txtLog.append("이동합니다.")
            dice_encounter = randint(0, 1)
            if dice_encounter == 1:
                CombatWindow.show()
                self.hide()
                CombatWindow.spawning_monster()
            else:
                player.stats[7] += 2
                if player.stats[7] >= player.stats[8]:
                    player.stats[7] = player.stats[8]
                self.txtLog.append("아무것도 보이지 않아서 앉아서 휴식합니다.\n체력을 2 회복합니다. "+ str(player.stats[7])+" / "+str(player.stats[8])+"\n")

    def printTextFunction(self):
        print(self.lbl_Stat.text())
    
    def itemUse(self):
        if isinstance(player, NoClass) == True:
            self.btn_Charselect.setEnabled(False)
            myWindow.hide()
            CharWindow.show()
        else:
            dice_encounter = randint(0, 1)
            if dice_encounter == 1:
                
                self.txtLog.append("물약을 사용하려 했으나 적이 공격해 옵니다!!")
                CombatWindow.txtCombatLog.append("물약을 사용하려 했으나 적이 공격해 옵니다!!")
                
                CombatWindow.show()
                self.hide()
                CombatWindow.spawning_monster()
            else:
                self.txtLog.append("물약을 사용하여, 체력을 회복합니다.\n")
                if player.stats[7] >= player.stats[8]:
                        player.stats[7] = player.stats[8]
                else:
                    player.stats[7] += 5
                self.update_stats()

class CombatWindowClass(QWidget, widgetcombat_class):
    monster_hp = 0
    monster_init_hp = 0
<<<<<<< HEAD
    monster_name = ""
    monster_num = 0
    monster_speed = 1
    initTimer = 0
=======
>>>>>>> parent of 66b6bd8 (Add files via upload)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):        
        self.btn_CombatAttack.clicked.connect(self.combat_attack)
        self.btn_CombatSkill.clicked.connect(self.combat_skill)
        self.btn_CombatFlee.clicked.connect(self.combat_flee)
        self.bar_monsterhp.setMinimum(0)
        self.bar_playerhp.setMinimum(0)
    
<<<<<<< HEAD
    def combat_start(self, CombatRunning=False):
        if CombatRunning == True:
            self.monster_num = self.monster_max_num = randint(1, 3)
            self.combat_running = True
            self.clicker_start()
        else:
            pass
    
    def clicker_start(self):
        self.timer = QTimer()
        if self.combat_running == True:
            self.timer.start()
            self.timer.setInterval((6-self.monster_speed) * 1000)
            self.timer.timeout.connect(self.monster_attack)
        else:
            self.timer.stop()

    def monster_attack(self):
        self.monster_damage = randint(1, 3)
        player.stats[7] -= self.monster_damage 
        if player.stats[7] <= 0: player.stats[7] = 0 # - 수치를 0으로 바꿔줌
        
        combatmsg2 = f"{self.monster_name}에게 <span style='color: red'><b> {str(self.monster_damage)}</span></b> 의 피해를 입습니다!!\n"
        # combatmsg2 = str(f"으악!! "+self.monster_name+"에게 "+"<p style='color: red'>"+str(self.monster_damage)+"</p>"+"의 피해를 입습니다!!\n")
        self.txtCombatLog.append(combatmsg2)
        myWindow.txtLog.append(combatmsg2)
        self.update()

    def spawning_monster(self):
        monsters = "코볼트", "고블린", "좀비", "구울"
        self.monster_name = choice(monsters)
        self.monster_speed = randint(1, 5)
        self.monster_hp = randint(1, 30)
        self.monster_init_hp = self.monster_hp
        self.txtCombatLog.clear()
        msgSpawning = f"{self.monster_name}가 나타납니다. <span style='color: red'>({self.monster_num}/{self.monster_max_num})</span>"
        myWindow.txtLog.append(msgSpawning)
        CombatWindow.txtCombatLog.append(msgSpawning)
=======
    def spawning_monster(self):
        self.txtCombatLog.clear()
        monsters = "코볼트", "고블린", "좀비", "구울"
        self.monster_name = choice(monsters)
        msg_monster = self.monster_name+"을(를) 만났습니다!!"       #매세지 작업
        self.txtCombatLog.setPlainText(msg_monster)
        myWindow.txtLog.append(msg_monster)
       
        if self.monster_hp == 0:
            self.monster_hp = randint(1, 30)
            self.monster_init_hp = self.monster_hp
>>>>>>> parent of 66b6bd8 (Add files via upload)
        self.update()

    def update(self):
        self.lbl_monsterhp.setText(str(self.monster_hp)+"/"+str(self.monster_init_hp))
        self.lbl_playerhp.setText(str(player.stats[7])+"/"+str(player.stats[8]))
        self.bar_monsterhp.setValue(self.monster_hp)
        self.bar_monsterhp.setMaximum(self.monster_init_hp)        # Monster HP
        self.bar_monsterhp.setValue(self.monster_hp)
        self.bar_playerhp.setMaximum(player.stats[8])     # Player HP
        self.bar_playerhp.setValue(player.stats[7])
    
    def combat_attack(self):
<<<<<<< HEAD
        for x in range(0, player.mulAttack):
            player_damage = randint(int(player.stats[1] / 2 / 5), int(player.stats[1]/5))
    
            self.monster_hp -= player_damage
            if self.monster_hp <= 0: self.monster_hp = 0 # - 수치를 0으로 바꿔줌
            combatmsg1 = f"<span style='color: blue'><b>{str(player_damage)}</span></b>의 피해를 입힙니다!!({player.skillName})"
            self.txtCombatLog.append(combatmsg1)
            self.update()
            if self.monster_hp <= 0:
                self.monster_num_sub()
    
    def monster_num_sub(self):
        self.monster_num -= 1
        if self.monster_num == 0:
            self.timer.stop()
            self.combat_victory()
        else:
            self.spawning_monster()

=======
        player_damage = randint(int(player.stats[1] / 2), player.stats[1])
        monster_damage = randint(1, 3)

        self.monster_hp -= player_damage
        if self.monster_hp <= 0: self.monster_hp = 0 # - 수치를 0으로 바꿔줌

        combatmsg1 = str("에잇!! "+self.monster_name+"에게 "+str(player_damage)+"의 피해를 입힙니다!!")
        self.txtCombatLog.append(combatmsg1)
        myWindow.txtLog.append(combatmsg1)
        player.stats[7] -= monster_damage 
        
        if player.stats[7] <= 0: player.stats[7] = 0 # - 수치를 0으로 바꿔줌
        
        combatmsg2 = str("으악!! "+self.monster_name+"에게 "+str(monster_damage)+"의 피해를 입습니다!!\n")
        self.txtCombatLog.append(combatmsg2)
        myWindow.txtLog.append(combatmsg2)
        self.update()
        if self.monster_hp == 0:
            self.combat_victory()
    
>>>>>>> parent of 66b6bd8 (Add files via upload)
    def combat_skill(self):
        self.skill_timer = QTimer()
        self.skill_timer.start()
        self.skill_timer.setInterval(1000)
        self.skill_timer.timeout.connect(self.skillTimer)
        player.skill_01()

        self.txtCombatLog.append(f"<span style='color: green'>{player.skillName}</span> 시전합니다!!")
        self.btn_CombatSkill.setText("활성화!!")
    
    def skillTimer(self):
        self.initTimer += 1
        if self.initTimer == player.skillDuration:
            player.skill_00()
            self.btn_CombatSkill.setText("스킬1")

    def combat_victory(self):
<<<<<<< HEAD
        self.combat_reset()
        self.hide()
        player.stats[6] += self.monster_max_num * 10
        myWindow.txtLog.append("\n"+str(self.monster_max_num * 10)+"의 경험치를 획득하였습니다.")
=======
        CombatWindow.hide()
        player.stats[6] += 10
>>>>>>> parent of 66b6bd8 (Add files via upload)
        if player.stats[6] >= player.stats[5]*20:
            player.levelup()
        myWindow.show()
        myWindow.update_stats()
    
    def combat_flee(self):
        CombatWindow.close()
        myWindow.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '확인', '게임을 종료합니다.',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()

<<<<<<< HEAD
    def combat_reset(self):
        player.skill_00()      # 플레이어 스킬 초기화
        
=======
'''class CombatResultClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("계속 진행하시려면 클릭하세요.")
        self.selfText("This is the main text!") '''
>>>>>>> parent of 66b6bd8 (Add files via upload)

if __name__ == "__main__" :
    app = QApplication(sys.argv)   #QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()       #WindowClass의 인스턴스 생성
    CharWindow = CharWindowClass()
    CombatWindow = CombatWindowClass()
#    PauseWindow = CombatResultClass()
    myWindow.show()                #프로그램 화면을 보여주는 코드
    app.exec_()                    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드