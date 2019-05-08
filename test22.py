'''
计算100以内偶数纸盒.
continue是跳过本次循环剩余部分,hui
'''
a=0
b=0

while b<10:
    b+=1
    print('1b=',b)
    print('_'*10)
    if b % 2 ==1:
        continue
    a+=b
    print('2b=',b)
    print('1a=',a)
print('final a=',a)