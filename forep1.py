'''
菲薄那数列
'''
aa=input("请输入次数:")
number=int(aa)
alist=[]
a=-1
b=1
for i in range(0,number):
   c=a+b
   alist+=[c]
   a=b
   b=c
print(alist)
