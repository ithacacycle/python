'''
成绩分类
'''
score= int(input('亲 您的分数是:'))

if score >= 60 and score < 70:
    print('及格')
elif 70<= score <80:
    print('良')
elif 80 <= score < 90:
    print('好')
elif score >= 90:
    print('优秀')
else:
    print('弟弟 放弃吧')