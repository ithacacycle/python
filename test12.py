import getpass

username = input('username: ')
password = getpass.getpass('password')

if username == 'bob' and password == '123456':
    print('login successful')
else:
    print('login incorrect')