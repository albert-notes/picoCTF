from pwn import *

r=remote('mercury.picoctf.net',22902)
flag=""

while True:
    k=r.recvline().strip().decode()
    if k=="10":
        break
    else:
        flag+=chr(int(k))

print(flag)
