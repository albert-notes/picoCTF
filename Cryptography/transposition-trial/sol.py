with open('./message.txt','r') as f:
    cipher=f.read()

flag=""
for i in range(0,len(cipher),3):
    flag+=cipher[i+2]+cipher[i]+cipher[i+1]

print(flag)
