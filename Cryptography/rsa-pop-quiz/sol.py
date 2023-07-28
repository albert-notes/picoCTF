from pwn import *
from Crypto.Util.number import *

r=remote('jupiter.challenges.picoctf.org',58617)
r.recvline()
r.recvline()
r.recvline()
r.recvline()

#Q1
r.recvline()
q=int(r.recvline().strip().decode().split(' : ')[1])
p=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','Y')
r.recvline()
r.sendlineafter(b':',str(p*q).encode())
r.recvline()
r.recvline()
r.recvline()

#Q2
r.recvline()
p=int(r.recvline().strip().decode().split(' : ')[1])
n=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','Y')
r.recvline()
r.sendlineafter(b':',str(n//p).encode())
r.recvline()
r.recvline()
r.recvline()

#Q3
r.recvline()
e=int(r.recvline().strip().decode().split(' : ')[1])
n=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','N')
r.recvline()
r.recvline()
r.recvline()

#Q4
r.recvline()
q=int(r.recvline().strip().decode().split(' : ')[1])
p=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','Y')
r.recvline()
r.sendlineafter(b':',str((p-1)*(q-1)).encode())
r.recvline()
r.recvline()
r.recvline()

#Q5
r.recvline()
pln=int(r.recvline().strip().decode().split(' : ')[1])
e=int(r.recvline().strip().decode().split(' : ')[1])
n=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','Y')
r.recvline()
r.sendlineafter(b':',str(pow(pln,e,n)).encode())
r.recvline()
r.recvline()
r.recvline()

#Q6
r.recvline()
c=int(r.recvline().strip().decode().split(' : ')[1])
e=int(r.recvline().strip().decode().split(' : ')[1])
n=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','N')
r.recvline()
r.recvline()
r.recvline()

#Q7
r.recvline()
q=int(r.recvline().strip().decode().split(' : ')[1])
p=int(r.recvline().strip().decode().split(' : ')[1])
e=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','Y')
r.recvline()
phi=(p-1)*(q-1)
d=inverse(e,phi)
r.sendlineafter(b':',str(d).encode())
r.recvline()
r.recvline()
r.recvline()

#Q8
r.recvline()
p=int(r.recvline().strip().decode().split(' : ')[1])
c=int(r.recvline().strip().decode().split(' : ')[1])
e=int(r.recvline().strip().decode().split(' : ')[1])
n=int(r.recvline().strip().decode().split(' : ')[1])
r.recvline()
r.recvline()
r.sendlineafter(b':','Y')
r.recvline()
q=n//p
phi=(p-1)*(q-1)
d=inverse(e,phi)
r.sendlineafter(b':',str(pow(c,d,n)).encode())
print(long_to_bytes(pow(c,d,n)))