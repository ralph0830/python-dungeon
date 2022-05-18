from random import *
import os

class event_forest:
    def __init__(self):
        self.event_msg = "당신은 워리어로 태어났다."
    
    def event_stage1(self):
        eventDice = randint(1, 10)
        if eventDice == 1:
            self.event_msg = "\n울창한 숲 속에서 당신은 길을 잃었다.\n날씨는 매우 화창한 오후였으나, 하늘을 향해 쭉 뻗은 나무들이 햇빛을 모두 가려, 음산한 분위기가 연출되고 있었다.\n당신은 휴식을 취하고, 모닥불을 정리하였다. 이제 어떻게 할 것인가?\n"
        elif eventDice == 2:
            self.event_msg = "\n여기는 어디지? 당신은 깜깜한 숲 속에서 헤매고 있다.\n"
        elif eventDice == 3:
            self.event_msg = "\n""파스스"" 발에 나뭇가지가 부서지는 소리가 들린다.\n얼마나 걸었을까? 발이 아프다."
        elif eventDice == 4:
            self.event_msg = "\n앞에 흐릿하게 사람의 형상이 보인다. 무엇일까?"
        elif eventDice == 5:
            self.event_msg = "\n장비를 정비하고 길을 나선다.\n점점 두려워진다."
        elif eventDice == 6:
            self.event_msg = "\n여기는 어디고 나는 누구인지...헷갈린다."
        elif eventDice == 7:
            self.event_msg = "\n배가 고프다. 음식을 찾아봐야겠다."
        elif eventDice == 8:
            self.event_msg = "\n끝이 보이지 않는 숲에 당신은 감탄을 하였다.\n도대체 끝은 어디일까?"
        elif eventDice == 9:
            self.event_msg = "\n숲..숲..숲.. 며칠째인지 가늠이 되지 않는다."
        elif eventDice == 10:
            self.event_msg = "\n사랑을 했다. 우리가 만나 지우지 못할 추억이 됐다."
        return self.event_msg