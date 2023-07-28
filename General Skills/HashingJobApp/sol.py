from pwn import *
from hashlib import *

r=remote('saturn.picoctf.net',63116)

k=r.recvline().strip().split(b'\'')[1]
r.recvline()
m=hashlib.md5()
m.update(k)
r.sendline(m.hexdigest())
r.recvline()
r.recvline()

k=r.recvline().strip().split(b'\'')[1]
r.recvline()
m=hashlib.md5()
m.update(k)
r.sendline(m.hexdigest())
r.recvline()
r.recvline()

k=r.recvline().strip().split(b'\'')[1]
r.recvline()
m=hashlib.md5()
m.update(k)
r.sendline(m.hexdigest())
r.recvline()
r.recvline()
print(r.recvline())
