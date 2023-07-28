from Crypto.Util.number import *
from pwn import *

r=remote('mercury.picoctf.net',30048)
r.recvline()
r.recvline()
r.recvline()
r.recvline()
n=int(r.recvline().strip().split(b': ')[1])
e=int(r.recvline().strip().split(b': ')[1])
c=int(r.recvline().strip().split(b': ')[1])
cs=n-c
r.sendlineafter("Give me ciphertext to decrypt: ",str(cs))
m=n-int(r.recvline().strip().split(b': ')[1])
print(long_to_bytes(m))
