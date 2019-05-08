'''
先给定两个数字,后面数字总和是前两个数字之和
'''

f=[0,1]

for i in range(8):
    f.append(f[-1]+f[-2])
    print(f)
print(f)