#10 + 5的结果放到列表中
print([10+5])
#10 + 5这个表达是计算10次
print([10 + 5 for i in range(10)])
print([10+i for i in range(10)])
print([10+i for i in  range(1,11)])
#通过if过滤,满足if条件的猜参与10+i的运算
print([10 + i for i in range(1,11) if i%2==1])
print([10 + i for i in range(1,11) if i%2])
print(['192.168.1.%s' %i for i in range(1,255)])