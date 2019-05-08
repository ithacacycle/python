'''
end="\t"
就是 以空格结尾
else就是判断循环完了
就打印空的 就 换行了
'''
for i in range(1,10):
    for j in range(1,i+1):
        k=i*j
        print(i,'*',j,'=',k,end="\t")
    else:
        print("")

