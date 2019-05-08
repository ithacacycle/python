sum100 = 0
counter = 1

while counter <101:
  sum100 += counter
  counter +=1
print(sum100)
'''
num=int(input('请输入想要累加的数: '))
anwer=((1+num)*num)/2
print(anwer)
'''


a,b=0,0
for i in range(1,101):
   a,b=a+b,b+i
print(b)