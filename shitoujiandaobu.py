import random
aliist = ['剪刀','石头','布']

x = random.randint(0,2)
computer=aliist[x]
print(
    '''
    0:剪刀
    1:石头
    2:布
    '''
)
print(x)
y=input('guest number[0-2]:')
y=int(y)
if y >=0 and y <=3:
    if int(y)==0 and x==2:
        print('你赢了')
    elif x == y :
        print('恭喜你平局')
    elif y==0 and x==1:
        print('你输了')
    elif y==1 and x==2:
        print('你输了')
    elif y==1 and x==0:
        print('你赢了')
    elif y ==2 and x==1:
        print('你输了')
    elif y ==2 and x==0:
        print('你赢了')

else:
    print('你犯规了')

    '''
      方法上的简写在if 判断里的简写
     if x==y:
       res = '平局'
     if y==0:
       res = '赢了' if x==2 else '输了'
     if y==1:
       res = '赢了' if x==0 else '输了'
      if y==2
       res = '赢了' if x==1 else '输了'
     print(res)
    '''
    '''
     逻辑上的简写  因为结果只有三种
     blist 里 枚举了赢的结果  增加一组b 列表 表示赢的结果
     
    '''
'''
import random

aliist = ['剪刀','石头','布']
blist =[(0,1),(1,2),(2,0)]

x = random.randint(0,2)
print(
    '''
    0:剪刀
    1:石头
    2:布
    '''
)
print(x)
y=input('guest number[0-2]:')
y=int(y)
if y >= 0 and y<3:
    res='赢了' if (x,y) in blist else '输了'
    if x==y:
        res == '平局'
    print(res)
else:
    print('你犯规了')
'''