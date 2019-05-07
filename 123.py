sentence = 'tom\' s pet is a cat '
sentence2 ="tom's pet is a cat"
sentence3 = "tom said:\"hello world!\""
print(sentence,sentence2,sentence3)

words ='''
hello
world
abcd
'''
print(words)

py_str='python'
len(py_str)
print(py_str[0])
print('python'[0])
print(py_str[-1])
print(py_str[2:4])
print(py_str[2:])
print(py_str[:2])
print(py_str[:])
print(py_str[::2])
print(py_str[1::2])
print(py_str[::-1])

print(py_str + 'is good')
print(py_str *3)

print('t' in py_str)
print('th' in  py_str)
print('to' in py_str)
print('to' not in py_str )

alist = [10,20,30,'bob','alice',[1,2,3]]
print(len(alist))
print(alist[-1])
print(alist[-1][-1])
print([1,2,3][-1])
print(alist[-2][2])
print(alist[3:5])
print(10 in alist)
print('o' in  alist)
print(100 not in alist)
alist[-1]=100
alist.append(200)

atuple = (10,20,30,'bob','alice', [1,2,3])
print(len(atuple))
print(10 in atuple)
print(atuple[2])
print(atuple[3:5])

adict = {'name':'bob','age':23}
print(len(adict))
print('bob' in  adict)
print('name' in  adict)
adict['email']='bob@tedu.cn'
adict['age']=25

print(adict)