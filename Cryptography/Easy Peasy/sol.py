from pwn import *

r=remote('mercury.picoctf.net',20266)
r.recvline()
r.recvline()
fl_enc=bytes.fromhex(r.recvline().strip().decode())
fl=len(fl_enc)

def enc(m):
    r.sendlineafter("What data would you like to encrypt? ", m)
    r.recvline()
    return bytes.fromhex(r.recvline().decode())

def xor(x,y):
    return bytes(a^b for a,b in zip(x,y))

enc("a"*(50000-fl))
key_xor=enc("a"*fl)

flag=xor(fl_enc,xor(key_xor,b"a"*fl)).decode()
print("picoCTF{"+flag+"}")
