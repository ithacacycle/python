'''
系统随机生成100以内的数字
要求用户猜生成的数字是多少
最多猜5次 猜对程序结束
如果5次全部猜错 输出正确结果
'''

import random
print('''
 请输入您要猜的数字 
 100以内 
 只有5次机会
''')
x = random.randint(0,99)

time=0



while time<5:
  time += 1
  a=input('请输入您要猜的数字')
  user_intput=int(a)
  if user_intput>0 and user_intput < 100:
     if user_intput >x:
         print('您猜大了')
     elif user_intput < x:
         print('您猜小了')
     elif user_intput ==x:
         print('您猜对了')
         break
else:
      print('次数用完了')