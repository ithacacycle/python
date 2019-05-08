'''
猜数
'''

import random
num = random.randint(1,10)
answer =int(input('guess a number: '))
if answer > num:
    print('猜大了')
elif answer <num:
    print('猜小了')
else:
    print('猜对了')

print('the number is :',num)