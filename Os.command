#!/Users/hude/Library/Caches/activestate/bin/python3
import time
import os
print (" 𝙃𝙐𝘿𝙀 𝙊𝙎 ")
cwd = "/Users/Hude/Desktop/HUDE OS/user/"
print("""
[1]Setup
[2]Log in
""")
setup = input("[?]: ")
if setup == '1':
    name = input(str("ENTER YOUR USER NAME:"))
    pas = input(str("ENTER PASWORD:"))


    with open(cwd + 'username.txt', 'w') as f:
        f.writelines(name)


    with open(cwd + 'password.txt', 'w') as f:
        f.writelines(pas)
if setup == '2':
    login_pass = open(cwd + 'password.txt')
    login_name = open(cwd + 'username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()
while True:
    login = input(str("Please enter the Pasword to " + l_n + ":"))
    if login == l_p:
        os.system('python3 /Users/hude/Desktop/"HUDE OS"/home.py')
        break
    else:
        print("wrong pascode")
