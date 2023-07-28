from Crypto.Util.number import *
from pwn import *
import owiener

r=remote('mercury.picoctf.net',31133)
r.recvline()
e=int(r.recvline().strip().split(b': ')[1])
n=int(r.recvline().strip().split(b': ')[1])
c=int(r.recvline().strip().split(b': ')[1])

d=owiener.attack(e,n)
print(long_to_bytes(pow(c,d,n)))
