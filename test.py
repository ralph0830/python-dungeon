import sys
from random import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer

form_class = uic.loadUiType("test.ui")[0]

class WindowClass(QMainWindow, form_class):    #화면을 띄우는데 사용되는 Class 선언
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
                
    def initUI(self):
        self.lbl_01.setText("hello")
        self.lbl_02.setText("hello")

        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.printTime1)
        self.timer1.start(100)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.printTime2)
        self.timer2.start(2000)
        self.a = 0
        self.b = 3
    
    def printTime1(self):
        self.lbl_01.setText(str((self.a)))
        self.a += 1

    def printTime2(self):
        self.lbl_02.setText(str((self.b)))
        self.b += 1

if __name__ == "__main__" :
    app = QApplication(sys.argv)   # QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()       # WindowClass의 인스턴스 생성
    myWindow.show()                # 프로그램 화면을 보여주는 코드
    app.exec_()                    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드