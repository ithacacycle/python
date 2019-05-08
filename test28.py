import  random

all_choices = ['石头','剪刀','布']
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
prompt='''
(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2)
'''
cwin=0
pwin=0

while cwin < 2 and pwin <2 :
    computer = random.choice(all_choices)
    ind = int(input(prompt))
    player = all_choices[ind]
    print('Your choice: %s ,Conputer`s choice: %s' %(player,computer))
    if player == computer:
        print('平局')
    elif [player , computer] in win_list:
        pwin+=1
        print('你赢了了')
    else:
        cwin +=1
        print('你输了')