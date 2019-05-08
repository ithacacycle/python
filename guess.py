'''
系统随机生成100以内的数字
要求用户猜生成的数字是多少
最多猜5次 猜对程序结束
如果5次全部猜错 输出正确结果
'''
'''
import random

x = random.randint(0,99)

time=0

a=input('请输入您要猜的数字')
user_intput=int(a)
while time<5:
  if user_intput>0 and user_intput < 100:
     if user_intput >x:
         time +=1
         print('您猜大了')
     elif user_intput < x:
         print('您猜小了')
         time +=1
         continue
     elif user_intput ==x:
         print('您猜对了')
         break
  else:
      print('您的数字有问题')
      break
'''

import random

print('''
 请输入您要猜的数字 
 100以内 
 只有5次机会
''')
x = random.randint(0,99)
print(x)
number_list=[x]
i=5
while i:
    i-=1
    n=input('guess nimber x:')
    n=int(n)
    number_list.append(n)
    if x==n:
        print('猜对了','x= ',x,number_list)
        break
    elif x<n:
        print('大了')
    else:
        print('小了')
else:
    print('user guess:',number_list)