default_username='root'
default_password='123456'
username = input("localhost login:")
password = input('Password:')

if default_username == username:
    if default_password == password:
        print('welocme to' , username)
    else:
        print('password error !')
else:
    print('username error')