print("\t[사칙 연산 게임을 시작합니다.]")
print("\t\t<게임 룰 소개>")
print("-> 숫자 3개, 기호 2번 사용하여 수식을 만들어 숫자를 맞추는 게임 \n-> 스테이지마다 숫자 16개를 공개하며 이 숫자와 기호 2개를 이용해 진행자가 발표한 숫자를 맞추면 점수를 획득 \n-> 둘 중 한명이 11점을 먼저 획득한 사람이 최종 승리 \n-> 점수 획득 방법: 숫자 3번 기호 2번 쓸 경우 1점 획득|숫자 2번 기호 1번 쓸 경우 2점 획득")
print("-> 승점 2점 획득 이후부턴 수식이 틀릴 경우 1점 감점")
print("\n\t\t<게임 순서>") 
print("1. 가위바위보를 1번 진행하여 승자에게 찬스권 부여 - 찬스권:숫자 2개 기호 1번 쓸 수 있음 \n2. 숫자 16개 공개 후 진행자 숫자 발표 \n3. 맞춘 사람 승점 1점 획득 다음 스테이지로 이동 \n4. 11점 먼저 획득 시 최종 승리, 만약 10:10이 된다면 2점 차이가 날 때까지 스테이지를 추가 진행 \n")
print("\n\n\t\t<게임 시작>")
print("\t[먼저 가위바위보를 진행합니다.]")
print("\t[랜덤으로 가위바위보가 선택됩니다.]")

class human:
    def __init__(self,score):
        self.score=score

class player1(human):

    def score1_win(self):
        self.score+=1    
    def score1_false(self):
        self.score-=1
class player2(human):

    def score2_win(self):
        self.score+=1
    def score2_false(self):
        self.score-=1
PLAYER1=player1(0)
PLAYER2=player2(0)  

import random
x=random.randrange(1,4)
y=random.randrange(1,4)
stage=1


if (x==1 and y==3) or (x==2 and y==1) or (x==3 and y==2):
    print("player1이 이겼습니다. player1이 찬스권을 가져갑니다.")
    PLAYER1_CHANCE="YES"
    PLAYER2_CHANCE="NO"
elif (x==1 and y==2) or (x==2 and y==3) or (x==3 and y==1):
    print("player2가 이겼습니다. player2가 찬스권을 가져갑니다.")
    PLAYER1_CHANCE="NO"
    PLAYER2_CHANCE="YES"
else:
    print("비겼으므로 찬스권은 사라집니다.")  
    PLAYER1_CHANCE="NO"
    PLAYER2_CHANCE="NO"  

def game_progress():  
    m_number=int(input("진행자가 숫자를 발표합니다. 숫자: "))
    while True:
        w_guess,chance_n=input("PLAYER1이면 PLAYER1을 PLAYER2이면 PLAYER2를 입력하고 찬스권 사용을 원하실 경우 YES를, 필요없으면 NO라고 입력하세요.: ").split()
        
        if (w_guess=="PLAYER1" and PLAYER1_CHANCE=="NO" and chance_n=="YES") or (w_guess=="PLAYER2" and PLAYER2_CHANCE=="NO" and chance_n=="YES"):
            print("chance권을 보유하고 있지 않습니다. 다시 입력해주세요.")
        elif chance_n=="NO":
            print("찬스권이 없거나 사용하지 않습니다.")
            break    
        elif (w_guess=="PLAYER1" or w_guess=="PLAYER2") and (PLAYER1_CHANCE=="YES" or PLAYER2_CHANCE=="YES") and chance_n=="YES":
            print("!CHANCE!",w_guess,"는 stage=",stage,"에서 CHANCE를 사용합니다. 기호 1개와 숫자 2개로 수식을 완성할 수 있습니다.")
            break

    m_guess0=input("수식을 입력하시오: ")
    m_guess=eval(m_guess0)
    return  m_number,w_guess,m_guess

#게임 진행을 위한 숫자, 수식 입력함수, 찬스권 사용여부와 유무 확인  

def answer_right_false(w_guess,m_number,m_guess):

    if w_guess=="PLAYER1" and m_number==m_guess:
        print("정답입니다. 다음 스테이지로 넘어갑니다.")
        PLAYER1.score1_win()
    elif w_guess=="PLAYER2" and m_number==m_guess:
        print("정답입니다. 다음 스테이지로 넘어갑니다.")
        PLAYER2.score2_win()
    elif w_guess=="PLAYER1" and m_number!=m_guess:
        player2_guess0=input("틀렸습니다. 순서는 PLAYER2에게 돌아갑니다. \nplayer2가 생각하는 답을 입력하시오.:")
        PLAYER1.score1_false()
        player2_guess=eval(player2_guess0)
        answer_right_false("PLAYER2",m_number,player2_guess)           
    elif w_guess=="PLAYER2" and m_number!=m_guess:
        player1_guess0=input("틀렸습니다. 순서는 PLAYER1에게 돌아갑니다. \nplayer1이 생각하는 답을 입력하시오.:")
        PLAYER2.score2_false()
        player1_guess=eval(player1_guess0)
        answer_right_false("PLAYER1",m_number,player1_guess)
           
#정답 확인 후 포인트 획득or감소시킴. 틀렸을 경우 다시 재입력 요구

def over_score(stage):

        while PLAYER1.score==PLAYER2.score+2 or PLAYER1.score+2==PLAYER2.score:
            r_number=random.sample(range(1,50),16)
            print("\t\tstage:",stage)
            print(r_number)
            stage+=1
            m_number,w_guess,m_guess=game_progress()
            answer_right_false(w_guess,m_number,m_guess)
            
# 만약 마지막 스테이지에서 플레이어1과 플레이어2의 점수가 같을 경우 2점 차이 날 때까지 진행 

while True:
    if stage>=11:
        if PLAYER1.score==PLAYER2.score:
            print("!MATCH POINT!2점 차이가 날 때까지 게임을 계속 진행합니다.")
            over_score(stage)
            break
        break

    if PLAYER1.score==6 or PLAYER2.score==6:
        print("다음 스테이지를 진행할 필요가 없습니다.")
        break
    
    print("\t\tstage:",stage,"(현재스코어",PLAYER1.score,":",PLAYER2.score,")")
    r_number=random.sample(range(1,50),16)
    print(r_number)

    m_number,w_guess,m_guess=game_progress()
    answer_right_false(w_guess,m_number,m_guess)

    stage+=1    


print("\t\t최종 점수")
print("\tPLAYER1 : PLAYER2")
print("\t",PLAYER1.score,PLAYER2.score)
if PLAYER1.score>PLAYER2.score:
    print("\tPLAYER1이 승리하였습니다.\n게임을 종료합니다.")
else:
    print("\tPLAYER2가 승리하였습니다.\n게임을 종료합니다.") 