'''
成绩分类
'''
score = int(input('分数: '))

if score >= 90:
    print('你是爷爷')
elif score >= 80:
    print('你是爸爸')
elif score >= 70:
    print('你是哥哥')
elif score >= 60:
    print('你是弟弟')
else:
    print('弟中弟别挣扎了')
