'''
实现循环结构 要求三局两胜
 用户 和 电脑
  平局
 循环次数
'''

import random

gameliist = ['剪刀','石头','布']
winlist =[(0,1),(1,2),(2,0)]

user_result=computer_result=0
while True:
 x = random.randint(0,2)
 print(
        '''
        0:剪刀
        1:石头
        2:布
        
        '''
 )
 '''print(x)'''
 y=input('guest number[0-2]:')
 y=int(y)

 if y >= 0 and y<3:
    if x==y:
       print('平局',end='\n\n')
       continue
    if (x,y) in winlist:
       user_result +=1
       print('赢了一局')
    else:
        computer_result +=1
        print('你输了一局')
    if user_result ==2:
        print('you win')
        break
    elif computer_result ==2:
        print('you lose')
 else:
        print('你犯规了')