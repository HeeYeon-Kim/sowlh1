class human:
    def __init__(self,name,HP,MP):
        self.name=name
        self.HP=HP
        self.MP=MP

    def meet(self):
        print("안녕하세요.") 

class player(human):
    AD=40
    def att(self,enemy):
        attack=(player.AD)-(enemy.DP)
        enemy.HP-=attack    

class npc(human):
  
    def meet(self):
        print("반갑습니다.") 

class enemy(human):
    DP=20


monkey1=player('파란원숭이',100,100)
monkey2=npc('무지개원숭이',100,100)
monster=enemy('개',100,100)

while True:

    com=int(input('입력:'))

    if com==1:
      monkey1.meet()
      monkey2.meet()

    elif com==2:
       monkey1.att(monster)
       print(monkey1.HP)
       print(monkey2.HP)
       print(monster.HP)

    if monster.HP==0:
       print('개를 무찔렀습니다!파란 원숭이와 무지개 원숭이가 이겼으므로 게임을 종료합니다~')
       break 
   
        