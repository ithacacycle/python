'''
-1是倒数第一个
-2是倒数第二个
'''
aa=input("请输入个数")
number=int(aa)
alist=[0,1]
for i in range(number-2):
    x=alist[-1]+alist[-2]
    alist.append(x)
print(alist)