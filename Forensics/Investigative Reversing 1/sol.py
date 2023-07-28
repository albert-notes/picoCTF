a1="CF{An1_9a47141}`"
a2=[0x85,0x73]
a3="icT0tha_"

flag=[0]*26
flag[1]=a3[0]
a3=a3[1:]
flag[0]=chr(a2[0]-0x15)
a2=[0x73]
flag[2]=a3[0]
a3=a3[1:]
flag[5]=a3[0]
a3=a3[1:]
flag[4]=a1[0]
a1=a1[1:]
for i in range(6,10):
    flag[i]=a1[0]
    a1=a1[1:]
flag[3]=chr(a2[0]-4)
for i in range(10,15):
    flag[i]=a3[0]
    a3=a3[1:]
for i in range(15,26):
    flag[i]=a1[0]
    a1=a1[1:]

print("".join(i for i in flag))
