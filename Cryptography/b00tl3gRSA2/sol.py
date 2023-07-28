import owiener
from pwn import *
from Crypto.Util.number import *

r=remote('jupiter.challenges.picoctf.org',19566)
c=int(r.recvline().strip().decode().split(': ')[1])
n=int(r.recvline().strip().decode().split(': ')[1])
e=int(r.recvline().strip().decode().split(': ')[1])

d=owiener.attack(e,n)
print(long_to_bytes(pow(c,d,n)))
