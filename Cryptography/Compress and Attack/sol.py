from pwn import *
import string

flag='picoCTF{'
r=remote('mercury.picoctf.net',50899)

def exploit(text):
    r.recvuntil(': ')
    r.sendline(text)
    r.recvline()
    r.recvline()
    return int(r.recvline().decode())

length=exploit(flag)

cur=""
while cur!='}':
    for c in string.printable:
        if exploit(flag+c)==length:
            flag+=c
            cur=c
            print(flag)
            break
