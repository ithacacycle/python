'''
99乘法表
'''

for a in range(1,10):
    for b in range (1,a+1):
        print(a,'*',b,'=',a*b,end=' | ')
    print()
    print()

number=int(input('请制定×到多少'))

for c in range(1,number+1):
    for d in range(1,c+1):
        print('%s*%s=%s' %(c,d,c*d),end=' | ')
    print()
    print()