from Crypto.Util.number import *
from pwn import *
from sage.all import *

r=remote('jupiter.challenges.picoctf.org',4557)

c=int(r.recvline().strip().decode().split(': ')[1])
n=int(r.recvline().strip().decode().split(': ')[1])
e=int(r.recvline().strip().decode().split(': ')[1])

pr=list(str(factor(n)).split(' * '))
phi=1
for i in pr:
    phi*=int(i)-1
d=inverse(e,phi)
print(long_to_bytes(pow(c,d,n)))
