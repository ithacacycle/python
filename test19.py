'''
猜数,5次机会
'''
import random

num = random.randint(1,10)
counter = 0

print(num)
while counter < 5:
    answer = int(input('guess the number: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter +=1
else:
    print('The number is: ',num)