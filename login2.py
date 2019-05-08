default_username='root'
default_password='123456'
while True:
    ''' whilr True  就是  一直循环'''
    username = input("localhost login:")
    password = input('Password:')
    if    default_username == username and default_password == password:
        print('welocme to' , username)
        break
    else:
        print('密码错误')
    if  default_username != username:
        print('用户名错误')
