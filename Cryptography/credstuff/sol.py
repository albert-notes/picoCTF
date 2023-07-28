with open('./leak/usernames.txt','r') as f:
    user=list(f.read().split('\n'))
with open('./leak/passwords.txt','r') as f:
    pwd=list(f.read().split('\n'))

for i in range(len(user)):
    if user[i]=='cultiris':
        print(pwd[i])
