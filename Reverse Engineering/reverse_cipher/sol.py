flag_enc="picoCTF{w1{1wq85jc=2i0<}"
flag=""

for i in range(8):
    flag+=flag_enc[i]

for i in range(8,23):
    if i&1:
        flag+=chr(ord(flag_enc[i])+2)
    else:
        flag+=chr(ord(flag_enc[i])-5)

flag+="}"
print(flag)
